import sys
input = sys.stdin.readline

n = int(input().rstrip())

for i in range(9):
    print("{0} * {1} = {2}".format(n, i+1, n*(i+1)))