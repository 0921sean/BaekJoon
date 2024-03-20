import sys
input = sys.stdin.readline

pri = []
n = int(input().rstrip())

lst = list(map(int, input().split()))

for i in lst:
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if (i % j == 0):
            break
    else:
        pri.append(i)

print(len(pri))