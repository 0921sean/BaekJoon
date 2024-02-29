import sys

n = int(input())
lst = []
for _ in range(n):
    lst.append(sys.stdin.readline())

lst = sorted(set(lst))
lst.sort(key=len)

for i in lst:
    sys.stdout.write(str(i))