# n 최대가 300,000이라 메모리 초과 오류를 신경쓰지 않아도 됨
# import sys

# def my_round(val):
#     if (val - int(val) >= 0.5):
#         return int(val) + 1
#     else:
#         return int(val)
    
# input = sys.stdin.readline

# n = int(input().rstrip())
# m = my_round(n * 0.15)
# lst = [0] * 31

# if n == 0:
#     print(0)
# else:
#     for _ in range(n):
#         num = int(input().rstrip())
#         lst[num] += 1

#     n = n - 2 * m
#     bot = n
#     tot = 0

#     i = 0
#     while True:
#         if (m != 0):
#             if (m < lst[i]):
#                 lst[i] -= m
#                 m = 0
#                 # print(lst)
#             else:
#                 m -= lst[i]
#                 i += 1
#                 # print(lst)
#         else:
#             if (n <= lst[i]):
#                 tot += i * n
#                 n = 0
#                 # print(lst)
#                 break
#             else:
#                 tot += i * lst[i]
#                 n -= lst[i]
#                 i += 1
#                 # print(lst)

#     print(my_round(tot/bot))

import sys

def my_round(val):
    if (val - int(val) >= 0.5):
        return int(val) + 1
    else:
        return int(val)
    
input = sys.stdin.readline

n = int(input().rstrip())
lst = []

if n == 0:
    print(0)
else:
    for _ in range(n):
        num = int(input().rstrip())
        lst.append(num)

    lst.sort()

    m = my_round(n * 0.15)
    tot = 0

    for i in range(m, n-m):
        tot += lst[i]

    print(my_round(tot/(n-2*m)))