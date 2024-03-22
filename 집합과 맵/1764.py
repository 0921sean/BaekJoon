# # dict, list 사용
# import sys
# input = sys.stdin.readline

# # 입력 받기
# N, M = map(int, input().split()) # 듣도 못한 사람 수, 보도 못한 사람 수
# dct = {} # 듣도 못한 사람 dict
# lst = [] # 듣도 보도 못한 사람 리스트
# cnt = 0 # 듣도 보도 못한 사람 수

# # 듣도 못한 사람 dict 생성
# for i in range(N):
#     dct[input().rstrip()] = True

# # 듣도 보도 못한 사람 리스트 생성
# for i in range(M):
#     name = input().rstrip() # 이름
#     if name in dct:
#         lst.append(name)
#         cnt += 1

# lst.sort() # 사전순으로 출력 위해 정렬

# # 결과 출력하기
# print(cnt) # 듣보잡 수

# for i in lst:
#     print(i) # 듣보잡 명단 출력

# 집합 사용
import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split()) # 듣도 못한 사람 수, 보도 못한 사람 수

# 듣도 못한 사람 집합 생성
a = set()
for _ in range(N):
    a.add(input().rstrip())

# 보도 못한 사람 집합 생성
b = set()
for _ in range(M):
    b.add(input().rstrip())

res = sorted(list(a & b)) # 듣보잡 리스트 생성, 정렬

# 결과 출력하기
print(len(res)) # 듣보잡 수

for i in res:
    print(i) # 듣보잡 명단 출력