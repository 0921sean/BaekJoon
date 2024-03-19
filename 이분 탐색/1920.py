# # set 사용
# # 입력 받기
# N = int(input())
# A = set(map(int, input().split()))
# M = int(input())
# X_lst = list(map(int, input().split()))

# for X in X_lst:
#     if X in A:
#         print(1)
#     else:
#         print(0)

# 이분 탐색 사용
# 입력 받기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
X_lst = list(map(int, input().split()))

# 이분탐색을 위해 리스트 정렬
A.sort()

for X in X_lst:
    l, r = 0, N-1 # left, right 지점을 선택
    isExist = False

    # 이분탐색 시작
    while l <= r:
        m = (l + r) // 2 # 중간 지점을 mid로 선택
        if X > A[m]: # X가 mid보다 오른쪽에 있다면
            l = m + 1 # left 지점을 현재 mid 지점으로 이동
        elif X < A[m]: # X가 mid보다 왼쪽에 있다면
            r = m - 1 # right 지점을 현재 mid 지점으로 이동
        else: # X가 mid 지점 숫자라면
            isExist = True # X가 A 안에 존재함을 의미
            print(1)
            break

    if not isExist: # X가 A 안에 존재하지 않았을 경우
        print(0)