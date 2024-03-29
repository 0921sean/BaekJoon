import sys
input = sys.stdin.readline

# 입력 받기
T = int(input().rstrip()) # 테스트 케이스 수
lst = [0, 1, 1, 1, 2, 2] # P(N) 리스트
cnt = 5 # (리스트 길이) - 1

for _ in range(T):
    N = int(input().rstrip()) # P(N)의 N
    while (N > cnt):
        lst.append(lst[cnt] + lst[cnt-4])
        cnt += 1

    # 결과 출력하기
    print(lst[N])