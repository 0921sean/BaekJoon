import sys
input = sys.stdin.readline

s = set()
cnt = 0

n, m = map(int, input().split())

for i in range(n):
    wrd = input().rstrip()
    s.add(wrd)

for i in range(m):
    a = input().rstrip()
    if a in s:
        cnt += 1

print(cnt)