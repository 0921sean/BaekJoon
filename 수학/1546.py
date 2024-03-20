import sys
input = sys.stdin.readline

new_lst = []
n = int(input().rstrip())

lst = list(map(int, input().split()))
m = max(lst)

for i in lst:
    new_lst.append((i * 100) / m)

print(sum(new_lst) / len(new_lst))