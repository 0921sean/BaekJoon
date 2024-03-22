# 입력 받기
N = int(input().rstrip()) # 줄 서 있는 사람 수
times = list(map(int, input().split())) # 각 사람이 돈 인출하는 데 걸리는 시간 리스트
res = 0 # 필요한 시간의 합 최솟값

times.sort() # 정렬

for i in range(N):
    res += times[i] * (N-i)

# 결과 출력하기
print(res)