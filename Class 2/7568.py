# 첫번째 시도
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# lst = []
# dct = {}
# gra_lst = []

# for _ in range(n):
#     x, y = map(int, input().split())
#     lst.append(x)
#     dct[x] = y

# sort_lst = sorted(dct.items(), reverse=True)

# for i in range(len(lst)):
#     gra = 1
#     if (i != 0):
#         for j in range(0, i):
#             if (sort_lst[j][1] > sort_lst[i][1]):
#                 gra += 1
#     gra_lst.append(gra)

# for i in lst:
#     sort_lst.keys().index()

# print(gra_dct)

import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = []

for _ in range(n):
    w, h = map(int, input().split())
    lst.append((w, h))

for i in lst:
    rank = 1
    for j in lst:
        if (i[0] < j[0] and i[1] < j[1]):
            rank += 1
    print(rank, end=" ")