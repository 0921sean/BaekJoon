# 메모리 초과 발생
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# lst = []

# for _ in range(n):
#     num = int(input().rstrip())
#     lst.append(num)

# lst.sort()

# for i in lst:
#     print(i)

import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = [0] * 10001

for _ in range(n):
    num = int(input().rstrip())
    lst[num] += 1

for i in range(10001):
    l = lst[i]
    if l != 0:
        for j in range(l):
            print(i)