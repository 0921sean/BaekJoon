import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = []

for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

lst.sort()

for i in lst:
    print("{} {}".format(i[0], i[1]))