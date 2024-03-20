import sys
input = sys.stdin.readline

h, m = map(int, input().split())

if (m >= 45):
    m -= 45
elif (h == 0):
    h = 23
    m += 15
else:
    h -= 1
    m += 15

print("{} {}".format(h, m)) 