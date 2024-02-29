import sys
input = sys.stdin.readline

a = 1
b = 1
n, k = map(int, input().split())

for _ in range(k):
    a *= n
    b *= k
    n -= 1
    k -= 1

print(a // b)