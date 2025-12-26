#1
"""
N = int(input())

if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    a, b = 0, 1

    for _ in range(3, N + 1):
        a, b = b, a + b

    print(b)
"""
#2
"""
N = int(input())

dp = [0] * (N + 1)

dp[0] = 1

for i in range(1, N + 1):
    dp[i] = dp[i-1]
    if i >= 2:
        dp[i] += dp[i-2]
    if i >= 3:
        dp[i] += dp[i-3]

print(dp[N])
"""