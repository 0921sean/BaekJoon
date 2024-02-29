import sys
input = sys.stdin.readline

l = int(input().rstrip())
res = 0
n = 0

wrd = input().rstrip()

for i in wrd:
    res += (ord(i)-96) * (31**n)
    n += 1

print(res % 1234567891)