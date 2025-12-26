#1
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
        print("Да")
    elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
        print("Да")
    else:
        print("Нет")
else:
    print("Ошибка!")
    """
#2
"""
K = int(input())
N = int(input())

sum_even = 0

for num in range(K, N + 1):
    if num % 2 == 0:
        sum_even += num

print(sum_even)
"""
#3
"""
total = 0

while True:
    num = int(input())

    if num == 0:
        break

    total += num

print(total)
"""

#4
"""
N = int(input())

factorial = 1

for i in range(1, N + 1):
    factorial *= i

print(factorial)
"""





























