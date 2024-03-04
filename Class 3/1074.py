# import sys
# input = sys.stdin.readline

# N, r, c = map(int, input().split())

# lst = [[0]*(2**N) for _ in range(2**N)]
# cnt = 0

# # n: 사각형 변 길이, x: 시작 행, y: 시작 열
# def z(n, x, y):
#     if n != 2:
#         z(n/2, x, y)
#         z(n/2, x, y+n/2)
#         z(n/2, x+n/2, y)
#         z(n/2, x+n/2, y+n/2)
#     else:
#         lst[x][y] += cnt
#         lst[x][y+1] += cnt+1
#         lst[x+1][y] += cnt+2
#         lst[x+1][y+1] += cnt+3
#         cnt += 4

# z(2**N, 0, 0)
# print(lst)

# # 분할정복 측면
# import sys
# input = sys.stdin.readline

# N, r, c = map(int, input().split())
# cnt = 0

# while N > 1:
#     size = (2 ** N) // 2
#     if r < size and c < size:
#         pass
#     elif r < size and c >= size:
#         cnt += size ** 2
#         c -= size
#     elif r >= size and c < size:
#         cnt += size ** 2 * 2
#         r -= size
#     elif r >= size and c >= size:
#         cnt += size ** 2 * 3
#         r -= size
#         c -= size
#     N -= 1

# if r == 0 and c == 0:
#     print(cnt)
# if r == 0 and c == 1:
#     print(cnt + 1)
# if r == 1 and c == 0:
#     print(cnt + 2)
# if r == 1 and c == 1:
#     print(cnt + 3)

# 재귀함수
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def sol(N, r, c):
    if N == 0:
        return 0
    
    return 2*(r%2)+(c%2) + 4 * sol(N-1, int(r/2), int(c/2))

print(sol(N, r, c))