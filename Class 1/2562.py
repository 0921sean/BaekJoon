import sys
input = sys.stdin.readline

lst = [int(input().rstrip()) for _ in range(9)]

print(max(lst))
print(lst.index(max(lst)) + 1)