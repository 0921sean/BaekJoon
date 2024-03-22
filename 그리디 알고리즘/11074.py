import sys
input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().split()) # 갖고 있는 동전의 종류, 만들고자 하는 가치의 합
coins = [] # 동전 리스트
res = 0 # 필요한 동전 개수

# ex. coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
for _ in range(N):
    coins.append(int(input().rstrip()))
coins.sort(reverse=True) # 내림차순으로 정렬

for coin in coins:
    if coin <= K:
        cnt = K // coin # 추가되는 동전 개수
        K -= coin * cnt # K 조정
        res += cnt

# 결과 출력하기
print(res)