import sys
input = sys.stdin.readline

dct = {}

n = int(input().rstrip())

for i in list(map(int, input().split())):
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

m = int(input().rstrip())

find_lst = list(map(int, input().split()))

for i in find_lst:
    if i in dct:
        print(dct[i], end=" ")
    else:
        print("0", end=" ")