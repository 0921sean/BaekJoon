# 시간 초과
# import sys
# input = sys.stdin.readline

# dct = {}

# def fibonacci(n):
#     if (n == 0):
#         dct[0] += 1
#         return 0
#     elif (n == 1):
#         dct[1] += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# t = int(input().rstrip())

# for _ in range(t):
#     num = int(input().rstrip())
#     dct[0] = 0
#     dct[1] = 0
#     fibonacci(num)
#     print(dct[0], dct[1])

import sys
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    while (n >= len(zero)):
        zero.append(zero[-1] + zero[-2])
        one.append(one[-1] + one[-2])
    print(zero[n], one[n])