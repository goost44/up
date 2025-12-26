# 1
"""
def task_27686(filename):
    with open(filename, 'r') as f:
        text = f.read()

    max_len = 0
    current_len = 0

    for char in text:
        if char == 'X':
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0

    return max_len

if __name__ == "__main__":
    print(task_27686("27686.txt"))
"""
# 2
"""
def task_36037(filename):
    with open(filename, 'r') as f:
        text = f.read()

    max_len = 0
    current_len = 0
    i = 0
    n = len(text)

    while i < n:
        if i + 3 < n and text[i:i + 4] == "XZZY":
            max_len = max(max_len, current_len + 3)
            current_len = 0
            i += 4
        else:
            current_len += 1
            i += 1

    max_len = max(max_len, current_len)
    return max_len
if __name__ == "__main__":
    print(task_36037("36037.txt"))
"""

# 3
def task_46982(filename):
    with open(filename, 'r') as f:
        text = f.read()

    count = 0
    n = len(text)
    i = 0

    while i < n:
        if text[i] == 'E':
            length = 1
            has_f = False
            i += 1

            while i < n and text[i] != 'E':
                if text[i] == 'F':
                    has_f = True
                length += 1
                i += 1

            if i < n and text[i] == 'E':
                length += 1
                if length >= 12 and not has_f:
                    count += 1
            i += 1
        else:
            i += 1

    return count


if __name__ == "__main__":
    print(task_46982("46982.txt"))

