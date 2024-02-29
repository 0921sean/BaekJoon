import sys

input = sys.stdin.readline
n = int(input().rstrip())
lst = {}

lst = set(list(map(int, input().split())))

m = int(input().rstrip())

find_lst = []
find_lst = list(map(int, input().split()))

for i in find_lst:
    sys.stdout.write("{} ".format(int(i in lst)))