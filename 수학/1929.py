import sys
input = sys.stdin.readline

M, N = map(int, input().split())

# M부터 N까지 확인
for i in range(M, N+1):
    if i == 1: # 1은 소수가 아니므로 제외
        continue
    # '에라토스테네스의 체': 소수를 구할 떄 효율적인 방법
    for j in range(2, int(i**0.5)+1): # 2부터 루트i까지 (그 이상은 확인할 필요 없음)
        if i % j == 0: # 소수가 아님
            break
    else: # for문에 대한 else (for문이 다 돌 때까지 해결되지 않았음을 의미)
        print(i)