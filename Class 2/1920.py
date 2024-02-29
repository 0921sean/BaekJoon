import sys
input = sys.stdin.readline

dct = {}
n = int(input().rstrip())
a = set(input().split())

m = int(input().rstrip())
m_lst = input().split()

for i in m_lst:
    if i in a:
        print(1)
    else:
        print(0)