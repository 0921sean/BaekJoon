from collections import deque # BFS에서 사용
import sys
input = sys.stdin.readline

# 입력 받기
N, M, V = map(int, input().split()) # 정점 개수, 간선 개수, 탐색 시작 번호
lst = [[] for _ in range(N+1)] # 연결 리스트 생성
res_dfs = [] # DFS 리스트
res_bfs = [] # BFS 리스트

# 연결 정보 리스트 생성
for _ in range(M):
    a, b = map(int, input().split())
    lst[a] += [b]
    lst[b] += [a] # 양방향 연결

for i in lst:
    i.sort() # 정렬

# DFS
def dfs(v):
    if v not in res_dfs:
        res_dfs.append(v)
    for i in lst[v]:
        if i not in res_dfs:
            dfs(i)

dfs(V) # 함수 실행

# BFS
deq = deque([V]) # 큐 생성

while deq:
    v = deq.popleft()
    if v not in res_bfs:
        res_bfs.append(v)
    for i in lst[v]:
        if i not in res_bfs:
            deq.append(i)
            res_bfs.append(i)

# 결과 출력하기
for i in res_dfs:
    print(i, end=' ')

print('')

for i in res_bfs:
    print(i, end=' ')