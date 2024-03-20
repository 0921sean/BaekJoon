import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    ps = list(input().rstrip())
    i = 1
    while (i != len(ps) and len(ps) != 0):
        if (ps[0] == ')'):
            break
        if (ps[i] == ')'):
            ps.pop(i)
            ps.pop(i-1)
            i = 1
        else:
            i += 1
    if (len(ps) == 0):
        print("YES")
    else:
        print("NO")