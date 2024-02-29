import sys
input = sys.stdin.readline

m, n = map(int, input().split())

for i in range(m, n+1):
    # 1은 소수가 아니므로 제외
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if (i % j == 0):
            break
    else:
        print(i)