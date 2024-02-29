import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
h = 0
day = ((v-a-1) // (a-b)) + 2

print(day)