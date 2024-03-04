# 런타임 에러 발생
# 원인은 Ai 최대가 1,000,000인데 첫 번쨰로 K를 넘는 lst 요소를 찾는 과정에서 시간을 너무 많이 소모하는 게 아닐까 생각됨
# 아래 예시에서는 sort reverse를 해줘서 위의 과정이 매우 짧아짐
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# lst = []
# i = 0
# res = 0

# for _ in range(N):
#     lst.append(int(input().rstrip()))

# while True:
#     num = lst[i]
#     if num > K:
#         break
#     i += 1

# while (K != 0):
#     i -= 1
#     num = lst[i]
#     cnt = K // num
#     K -= cnt * num
#     res += cnt
# #     print('K:', K)
# #     print('res:', res)
    
# print(res)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input().rstrip()))
coins.sort(reverse=True)
# coins = [5000, 1000, 500, 100, 50, 10, 5, 1]

res = 0
for coin in coins:
    if coin <= K:
        cnt = K // coin
        K -= coin * cnt
        res += cnt

print(res)