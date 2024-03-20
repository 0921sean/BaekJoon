import sys
input = sys.stdin.readline

n = int(input().rstrip())

lst = list(map(int, input().split()))

print("{} {}".format(min(lst), max(lst)))