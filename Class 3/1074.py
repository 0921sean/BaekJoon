import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

lst = [[0]*(2**N) for _ in range(2**N)]
cnt = 0

# n: 사각형 변 길이, x: 시작 행, y: 시작 열
def z(n, x, y):
    if n != 2:
        z(n/2, x, y)
        z(n/2, x, y+n/2)
        z(n/2, x+n/2, y)
        z(n/2, x+n/2, y+n/2)
    else:
        lst[x][y] += cnt
        lst[x][y+1] += cnt+1
        lst[x+1][y] += cnt+2
        lst[x+1][y+1] += cnt+3
        cnt += 4

z(2**N, 0, 0)
print(lst)