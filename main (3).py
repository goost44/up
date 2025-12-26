# 1
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
if __name__ == "__main__":
    print(factorial(5))

# 2
"""
def remove_vowels(string):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return ''.join([char for char in string if char not in vowels])
if __name__ == "__main__":
    print(remove_vowels("Hello World!"))
    """
# 3
"""
def pascal(n):
    if n == 1:
        return [1]
    prev = pascal(n - 1)
    row = [1]
    for i in range(1, len(prev)):
        row.append(prev[i-1] + prev[i])
    row.append(1)
    return row

if __name__ == "__main__":
    print(pascal(6))
    """