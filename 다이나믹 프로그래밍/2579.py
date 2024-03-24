import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().rstrip()) # 계단의 개수

# 각 계단에 쓰여있는 점수 리스트
lst = [0] * 301
for i in range(1, N+1):
    lst[i] = int(input().rstrip())

# 다이나믹 프로그래밍 시작
dp = [0] * 301 # DP 테이블
dp[1] = lst[1]
dp[2] = lst[1] + lst[2]
dp[3] = max(lst[1] + lst[3], lst[2] + lst[3])

for i in range(4, N+1):
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])

# 결과 출력하기
print(dp[N])