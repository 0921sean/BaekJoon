import sys
input = sys.stdin.readline

n = int(input().rstrip())

lst = list(map(int, input().split()))

lst.sort()

res = 0
for i in range(n):
    res += lst[i] * (n-i)

print(res)