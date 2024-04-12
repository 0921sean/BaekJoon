import math

# 입력 받기
n = int(input()) # 자연수 n
dp = [0, 1] # 다이나믹 프로그래밍

for i in range(2, n+1):
    minValue = 1e9
    for j in range(1, int(math.sqrt(i))+1):
        minValue = min(minValue, dp[i - j**2])
    dp.append(minValue + 1)

# 결과 출력하기
print(dp[n])