import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = []

for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))

# 기준의 우선순위를 x[1]>x[0]으로 하는 방법
lst.sort(key = lambda x : (x[1], x[0]))

for i in lst:
    print("{} {}".format(i[0], i[1]))