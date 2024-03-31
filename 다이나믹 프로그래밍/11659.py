import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split()) # 수의 개수, 합 구해야 하는 횟수
lst = list(map(int, input().split())) # 주어진 수 리스트
sum_lst = [0] # 합 리스트
cnt = 0 # 합

for i in lst:
    cnt += i
    sum_lst.append(cnt)

for _ in range(M):
    i, j = map(int, input().split()) # i번째 수부터 j번째 수
    # 결과 출력하기
    print(sum_lst[j] - sum_lst[i-1]) # i번째부터 j번째 수까지의 합 = j번째 수까지의 합 - (i-1)번째 수까지의 합