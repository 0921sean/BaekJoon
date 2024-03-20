import sys
input = sys.stdin.readline

tot = 0
n = int(input().rstrip())
num = int(input().rstrip())

for _ in range(n):
    tot += (num % 10)
    num = num // 10
    
print(tot)