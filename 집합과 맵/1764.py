import sys
input = sys.stdin.readline

dct = {}
lst = []
cnt = 0
n, m = map(int, input().split())

for i in range(n):
    dct[input().rstrip()] = True

for i in range(m):
    name = input().rstrip()
    if name in dct:
        lst.append(name)
        cnt += 1

print(cnt)

lst.sort()

for i in lst:
    print(i)