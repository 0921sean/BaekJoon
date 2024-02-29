# # DFS
# import sys
# sys.setrecursionlimit(10000)

# input = sys.stdin.readline

# t = int(input().rstrip())

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs(x, y):
#     if (x <= -1 or x >= n or y <= -1 or y >= m):
#         return False
    
#     if lst[x][y] == 1:
#         lst[x][y] = 0

#         for i in range(4):
#             dfs(x + dx[i], y + dy[i])

#         return True
#     return False

# for _ in range(t):
#     m, n, k = map(int, input().split())

#     lst = [[0]*m for i in range(n)]

#     for _ in range(k):
#         x, y = map(int, input().split())
#         lst[y][x] = 1

#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if dfs(i, j):
#                 cnt += 1

#     print(cnt)

# BFS
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input().rstrip())

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue

            if lst[nx][ny] == 1:
                queue.append((nx, ny))
                lst[nx][ny] = 0

    return

for _ in range(t):
    m, n, k = map(int, input().split())

    lst = [[0]*m for i in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        lst[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)