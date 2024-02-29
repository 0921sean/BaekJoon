import sys
input = sys.stdin.readline

s = set()

for _ in range(10):
    num = int(input().rstrip())
    s.add(num % 42)

print(len(s))