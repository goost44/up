# 1

def task_39762(filename):
    with open(filename, 'r') as f:
        numbers = list(map(int, f.read().split()))

    count = 0
    max_sum = 0

    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i + 1]
        product = a * b
        sum_ab = a + b

        if product % 15 == 0 and sum_ab % 7 == 0:
            count += 1
            if sum_ab > max_sum:
                max_sum = sum_ab

    return count, max_sum
if __name__ == "__main__":
    result1 = task_39762("39762.txt")
    print(f"{result1[0]} {result1[1]}")

# 2
"""
def task_68279(filename):
    with open(filename, 'r') as f:
        numbers = list(map(int, f.read().split()))

    max_562 = 0
    for num in numbers:
        if num % 1000 == 562:
            if num > max_562:
                max_562 = num

    count = 0
    max_sum = 0

    for i in range(len(numbers) - 3):
        quadruple = numbers[i:i + 4]

        five_digit = sum(1 for x in quadruple if 10000 <= x <= 99999)
        if five_digit < 1 or five_digit > 2:
            continue

        mod3 = sum(1 for x in quadruple if x % 3 == 0)
        mod7 = sum(1 for x in quadruple if x % 7 == 0)
        if mod3 >= mod7:
            continue

        quadruple_sum = sum(quadruple)
        if max_562 < quadruple_sum < 2 * max_562:
            count += 1
            if quadruple_sum > max_sum:
                max_sum = quadruple_sum

    return count, max_sum
if __name__ == "__main__":
    result2 = task_68279("68279.txt")
    print(f"{result2[0]} {result2[1]}")
"""
# 3
"""
def task_40992(filename):
    with open(filename, 'r') as f:
        numbers = list(map(int, f.read().split()))

    odd_numbers = [x for x in numbers if x % 2 != 0]
    avg_odd = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

    count = 0
    max_sum = 0

    for i in range(len(numbers) - 1):
        a, b = numbers[i], numbers[i + 1]

        if not (a % 5 == 0 or b % 5 == 0):
            continue

        if not (a < avg_odd or b < avg_odd):
            continue

        count += 1
        pair_sum = a + b
        if pair_sum > max_sum:
            max_sum = pair_sum

    return count, max_sum


if __name__ == "__main__":
    result3 = task_40992("40992.txt")

    print(f"{result3[0]} {result3[1]}")
"""