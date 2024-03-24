# BFS
from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().rstrip()) # 컴퓨터 개수
V = int(input().rstrip()) # 연결된 컴퓨터 쌍 개수

lst = [[] for i in range(N+1)] # 연결 정보 리스트
virus = [0] * (N+1) # 각 컴퓨터가 바이러스에 걸렸는지 여부 리스트

# 연결 정보 리스트 생성
# ex. lst = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
for i in range(V):
    a, b = map(int, input().split()) # 연결되어 있는 컴퓨터 번호 쌍
    lst[a] += [b] # a에 b 연결
    lst[b] += [a] # b에 a 연결

virus[1] = 1 # 1번 컴퓨터는 감염
deq = deque([1]) # 큐 생성

while deq:
    num = deq.popleft() # num은 감염
    for i in lst[num]: # num에 연결된 i들에 대해
        if virus[i] == 0: # 감염되어 있지 않다면
            deq.append(i) # 다음 과정에서 i에 연결된 컴퓨터들을 확인하기 위해 큐에 추가
            virus[i] = 1 # i는 감염

# 결과 출력하기
print(sum(virus)-1) # 개수에서 1번 컴퓨터는 제외


# DFS
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().rstrip()) # 컴퓨터 개수
V = int(input().rstrip()) # 연결된 컴퓨터 쌍 개수

lst = [[] for i in range(N+1)] # 연결 정보 리스트
virus = [0] * (N+1) # 각 컴퓨터가 바이러스에 걸렸는지 여부 리스트

# 연결 정보 리스트 생성
# ex. lst = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
for i in range(V):
    a, b = map(int, input().split()) # 연결되어 있는 컴퓨터 번호 쌍
    lst[a] += [b] # a에 b 연결
    lst[b] += [a] # b에 a 연결

def dfs(v):
    virus[v] = 1 # v는 감염
    for i in lst[v]: # v에 연결된 i들에 대해
        if virus[i] == 0: # 감염되어 있지 않다면
            dfs(i) # i부터 시작해서 바이러스 감염

dfs(1) # 1번 컴퓨터부터 바이러스 시작

# 결과 출력하기
print(sum(virus)-1) # 개수에서 1번 컴퓨터는 제외