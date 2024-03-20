import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def GCD(x, y):
    if y > x:
        x, y = y, x
    while (y):
        x, y = y, x%y
    return x

def LCM(x, y):
    res = (x*y)//GCD(x, y)
    return res

print(GCD(a, b))
print(LCM(a, b))