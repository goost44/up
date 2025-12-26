# 1
def task1():
    for x in range(15):
        num1 = 1 * (15 ** 4) + 2 * (15 ** 3) + 3 * (15 ** 2) + x * (15 ** 1) + 5
        num2 = 1 * (15 ** 4) + x * (15 ** 3) + 2 * (15 ** 2) + 3 * (15 ** 1) + 3
        total = num1 + num2
        if total % 14 == 0:
            return total // 14
    return None


# 2
def task2():
    for p in range(2, 100):
        if p < 11:
            continue
        try:
            num1 = (10 * (p ** 6) + 11 * (p ** 5) + 2 * (p ** 4) + 6 * (p ** 3) + 7 * (p ** 2) + 13 * (p ** 1) + 1)
            num2 = (15 * (p ** 6) + 0 * (p ** 5) + 2 * (p ** 4) + 4 * (p ** 3) + 10 * (p ** 2) + 8 * (p ** 1) + 9)
            total = num1 + num2
            if total % (p - 1) == 0:
                return p
        except:
            continue
    return None


# 3
def task3():
    for x in range(10):
        num1 = x * (17 ** 3) + 11 * (17 ** 2) + 0 * (17 ** 1) + 9
        num2 = x * (15 ** 3) + 8 * (15 ** 2) + 14 * (15 ** 1) + 8
        total = num1 + num2
        if total % 155 == 0:
            return total // 155
    return None


# 4
def task4():
    min_val = float('inf')
    result = None

    for x in range(11):
        for y in range(11):
            if x >= 11 or y >= 11:
                continue
            if x >= 8 or y >= 8:
                continue

            num1 = y * (11 ** 4) + 0 * (11 ** 3) + 4 * (11 ** 2) + x * (11 ** 1) + 5
            num2 = 2 * (8 ** 4) + 5 * (8 ** 3) + 3 * (8 ** 2) + x * (8 ** 1) + y
            total = num1 + num2

            if total % 117 == 0 and total < min_val:
                min_val = total
                result = total // 117

    return result



