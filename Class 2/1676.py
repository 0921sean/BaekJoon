import sys
input = sys.stdin.readline

tot = 1
cnt = 0
n = int(input().rstrip())

while (n != 0):
    tot *= n
    n -= 1

while True:
    if (tot % 10 == 0):
        cnt += 1
    else:
        break
    tot = tot // 10

print(cnt)