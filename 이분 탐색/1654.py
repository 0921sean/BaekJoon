import sys
input = sys.stdin.readline

# 입력 받기
K, N = map(int, input().split()) # 갖고 있는 랜선의 개수, 필요한 랜선의 개수
lst = [int(input().rstrip()) for _ in range(K)] # 랜선 길이 리스트 생성

# 이분탐색 시작
l, r = 1, max(lst) # left, right
while l <= r:
    m = (l + r) // 2 # mid
    cnt = 0 # 만들 수 있는 랜선의 개수
    for i in lst:
        cnt += (i // m)
    if cnt >= N: # 크거나 같은 랜선의 길이가 존재하는 경우
        l = m + 1 # left를 mid로 당김
    else: # 작은 랜선의 길이가 필요한 경우
        r = m - 1 # right를 mid로 당김

# 결과 출력하기
print(r)