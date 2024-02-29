import sys
input = sys.stdin.readline

cnt = 0
lst = list(map(int, input().split()))

for i in lst:
    cnt += i*i

print(cnt % 10)