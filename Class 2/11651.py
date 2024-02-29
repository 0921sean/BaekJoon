import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = []

for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

sort_lst = sorted(lst, key = lambda x : (x[1], x[0]))

for i in sort_lst:
    print("{} {}".format(i[0], i[1]))