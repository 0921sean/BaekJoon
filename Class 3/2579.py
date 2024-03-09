# 살짝 잘못 생각한 부분이 있음
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())

# lst = [0]

# for _ in range(n):
#     num = int(input().rstrip())
#     lst.append(num)

# # print(lst)

# l = len(lst)
# sco_lst = [0] * l

# for i in range(l):
#     # sco_lst[0] = 0
#     if (i == 0):
#         continue

#     # sco_lst[1] = lst[1]
#     elif (i == 1):
#         sco_lst[1] += lst[1]
#         cnt = 0
        
#     else:
#         if (cnt == 1):
#             sco_lst[i] += sco_lst[i-2] + lst[i]
#             cnt = 0
#         else:
#             if (sco_lst[i-1] > sco_lst[i-2]):
#                 sco_lst[i] += sco_lst[i-1] + lst[i]
#                 cnt = 1
#             else:
#                 sco_lst[i] += sco_lst[i-2] + lst[i]
#                 cnt = 0

# print(sco_lst[-1])

import sys
input = sys.stdin.readline

n = int(input().rstrip())

lst = [0] * 301

for i in range(1, n+1):
    lst[i] = int(input().rstrip())

dp = [0] * 301
dp[1] = lst[1]
dp[2] = lst[1] + lst[2]
dp[3] = max(lst[1] + lst[3], lst[2] + lst[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])

print(dp[n])