import sys
input = sys.stdin.readline

# 입력 받기
T = int(input().rstrip()) # 테스트 케이스 수

for _ in range(T):
    n = int(input().rstrip()) # 정수
    dp = [0] * 11 # DP 테이블
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, 11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    # 결과 출력하기
    print(dp[n])