# 전체가 빠짐없이 체크되지 않음
# import sys
# input = sys.stdin.readline

# m = int(input().rstrip())
# dct = {}

# dct[1] = True
# for i in range(2, m+1):
#     dct[i] = False

# n = int(input().rstrip())
# lst = []
# for _ in range(n):
#     lst.append(list(map(int, input().split())))

# for i in lst:
#     if (dct[i[0]] or dct[i[1]]):
#         dct[i[0]] = True
#         dct[i[1]] = True

# cnt = 0
# for i in dct.values():
#     if (i == True):
#         cnt += 1
# print(cnt - 1)

# # BFS
# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip()) # 컴퓨터 개수
# v = int(input().rstrip()) # 연결선 개수

# graph = [[] for i in range(n+1)] # 그래프 초기화
# visited = [0] * (n+1) # 방문한 컴퓨터인지 표시

# for i in range(v): # 그래프 생성
#     a, b = map(int, input().split())
#     graph[a] += [b] # a에 b 연결
#     graph[b] += [a] # b에 a 연결 -> 양방향

# visited[1] = 1 # 1번 컴퓨터부터 시작이니 방문 표시
# Q = deque([1])
# while Q:
#     c = Q.popleft()
#     for nx in graph[c]:
#         if visited[nx] == 0:
#             Q.append(nx)
#             visited[nx] = 1
# print(sum(visited)-1)

# DFS
import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 컴퓨터 개수
v = int(input().rstrip()) # 연결선 개수

graph = [[] for i in range(n+1)] # 그래프 초기화
visited = [0] * (n+1) # 방문한 컴퓨터인지 표시

for i in range(v): # 그래프 생성
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 -> 양방향


def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)