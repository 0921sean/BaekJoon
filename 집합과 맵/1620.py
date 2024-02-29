import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dct = {}
for i in range(n):
    name = input().rstrip()
    dct[i] = name
    dct[name] = i

for i in range(m):
    que = input().rstrip()
    if que.isdigit():
        print(dct[int(que)-1])
    else:
        print(dct[que]+1)