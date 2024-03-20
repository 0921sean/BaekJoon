import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    if (lst[0] == 0):
        break
    c = max(lst[0], lst[1], lst[2])
    lst.remove(c)
    a, b = lst[0], lst[1]
    if (c**2 == a**2 + b**2):
        print("right")
    else:
        print("wrong")