# # 시간 초과
# import sys
# input = sys.stdin.readline

# # 입력 받기
# T = int(input().rstrip()) # 테스트 케이스 개수
# dct = {}

# # 피보나치 함수
# def fibonacci(n):
#     if (n == 0):
#         dct[0] += 1
#         return 0
#     elif (n == 1):
#         dct[1] += 1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# for _ in range(T):
#     fibonacci(int(input().rstrip()))
#     print(dct[0], dct[1]) # 결과 출력

import sys
input = sys.stdin.readline

# 입력 받기
T = int(input().rstrip())
zero = [1, 0, 1] # 0의 개수 리스트
one = [0, 1, 1] # 1의 개수 리스트

for _ in range(T):
    N = int(input().rstrip()) # N번째 피보나치
    while (N >= len(zero)):
        zero.append(zero[-1] + zero[-2])
        one.append(one[-1] + one[-2])
    print(zero[N], one[N])