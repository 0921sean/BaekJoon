# n 최대가 300,000이라 메모리 초과 오류를 신경쓰지 않아도 됨
# import sys

# def my_round(val):
#     if (val - int(val) >= 0.5):
#         return int(val) + 1
#     else:
#         return int(val)
    
# input = sys.stdin.readline

# n = int(input().rstrip())
# m = my_round(n * 0.15)
# lst = [0] * 31

# if n == 0:
#     print(0)
# else:
#     for _ in range(n):
#         num = int(input().rstrip())
#         lst[num] += 1

#     n = n - 2 * m
#     bot = n
#     tot = 0

#     i = 0
#     while True:
#         if (m != 0):
#             if (m < lst[i]):
#                 lst[i] -= m
#                 m = 0
#                 # print(lst)
#             else:
#                 m -= lst[i]
#                 i += 1
#                 # print(lst)
#         else:
#             if (n <= lst[i]):
#                 tot += i * n
#                 n = 0
#                 # print(lst)
#                 break
#             else:
#                 tot += i * lst[i]
#                 n -= lst[i]
#                 i += 1
#                 # print(lst)

#     print(my_round(tot/bot))

import sys
input = sys.stdin.readline

# 입력 받기
n = int(input().rstrip()) # 난이도 의견의 개수
lst = [] # 난이도 의견 리스트

# 직접 정의한 반올림 함수
def my_round(val):
    if (val - int(val) >= 0.5):
        return int(val) + 1
    else:
        return int(val)

if n == 0: # 특수한 경우 먼저 처리
    print(0)
else:
    # 난이도 의견 리스트 만듦
    for _ in range(n):
        lst.append(int(input().rstrip()))

    lst.sort() # 정렬

    m = my_round(n * 0.15) # 위아래 각각 제외할 난이도 의견 수
    res = 0 # 계산한 문제 난이도

    for i in range(m, n-m):
        res += lst[i]

    # 결과 출력하기
    print(my_round(res / (n-2*m)))