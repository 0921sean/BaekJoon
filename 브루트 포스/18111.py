# import sys
# input = sys.stdin.readline

# n, m, b = map(int, input().split())
# lst = []
# time = [0 for _ in range(257)]
# height = 0

# for _ in range(n):
#     lst.append(list(map(int, input().split())))

# # i : 맞출 높이
# for i in range(257):
#     block = b
#     temp = True
#     for x in range(n):
#         for y in range(m):
#             h = lst[x][y]
#             if (h >= i):
#                 time[i] += 2 * (h - i)
#                 block += (h - i)
#             else:
#                 time[i] += (i - h)
#                 block -= (i - h)
#     if (block >= 0 and time[i] <= time[height]):
#         height = i

# print(time[height], height)

# import sys
# input = sys.stdin.readline

# n, m, b = map(int, input().split())
# lst = []

# for _ in range(n):
#     lst.extend(map(int, input().split()))

# time = [0 for _ in range(257)]
# height = 0

# for i in range(257):
#     block = b
#     for h in lst:
#         if (h >= i):
#             time[i] += 2 * (h - i)
#             block += (h - i)
#         else:
#             time[i] += (i - h)
#             block -= (i - h)
#     if (block >= 0 and time[i] <= time[height]):
#         height = i

# print(time[height], height)

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
h_dct = {h : 0 for h in range(257)}
lst = []

for _ in range(n):
    temp = list(map(int, input().split()))
    for h in temp:
        h_dct[h] += 1

h_dct = list(h_dct.items())
time_lst = []

for i in range(257):
    over = [(k, v) for k, v in h_dct if k > i and v != 0]
    under = [(k, v) for k, v in h_dct if k < i and v != 0]
    time = 0
    block = b

    for h, cnt in over:
        time += 2 * (h - i) * cnt
        block += (h - i) * cnt
    for h, cnt in under:
        time += (i - h) * cnt
        block -= (i - h) * cnt

    if block < 0:
        break
    time_lst.append(time)

min_time = min(time_lst)
# time_lst에 time이 append되지 않는, block < 0인 경우는 맞출 높이가 너무 높아서임
# 따라서 time_lst의 idx가 곧 맞출 높이를 의미함
max_h_idx = [idx for idx, t in enumerate(time_lst) if t == min_time]
max_h = max(max_h_idx)

print(min_time, max_h)