# Задача 1: Наибольшая возрастающая подпоследовательность
"""
def lis_length(seq):
    n = len(seq)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(lis_length([6, 2, 5, 4, 2, 5, 6]))
"""
#2
"""
def main():
    # Чтение входных данных
    import sys
    data = sys.stdin.read().strip().split()

    if not data:
        return

    n = int(data[0])
    if n == 0:
        print(0)
        return

    sequence = list(map(int, data[1:n + 1]))

    # Алгоритм нахождения НВП
    dp = [1] * n  # dp[i] - длина наибольшей возрастающей подпоследовательности, заканчивающейся в i

    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    # Ответ - максимальное значение в dp
    print(max(dp))


if __name__ == "__main__":
    main()
"""
#3
# Задача 3: K-удивительные числа для K=1050
def reverse_number(n):
    return int(str(n)[::-1])

def count_k_amazing(k):
    count = 0
    for x in range(1, k):
        rev_x = reverse_number(x)
        if x + rev_x == k:
            count += 1
    return count

print(count_k_amazing(1050))





