import sys
input = sys.stdin.readline

k = int(input().rstrip())
stack = []
res = 0

for _ in range(k):
    num = int(input().rstrip())
    if num != 0:
        stack.append(num)
        res += num
    else:
        num = stack.pop()
        res -= num

print(res)