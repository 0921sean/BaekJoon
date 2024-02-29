import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lst = [int(input().rstrip()) for _ in range(k)]
l, r = 1, max(lst)

while (l <= r):
    m = (l + r) // 2
    cnt = 0
    for i in lst:
        cnt += (i // m)
    if cnt >= n:
        l = m + 1
    else:
        r = m - 1

print(r)