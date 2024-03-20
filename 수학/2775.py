import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    k = int(input().rstrip())
    n = int(input().rstrip())
    num = 1
    den = 1

    for i in range(k+1):
        num *= n
        n += 1
        den *= (i+1)
    
    print(num // den)