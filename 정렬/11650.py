import sys
n = int(input())
lst = []

for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort()

for i in lst:
    sys.stdout.write("{} {}\n".format(str(i[0]), str(i[1])))