import sys
input = sys.stdin.readline

s = input().rstrip()

lst = [i for i in s]

for i in range(26):
    alp = chr(i+97)
    if alp in lst:
        print(lst.index(alp), end=" ")
    else:
        print("-1", end=" ")