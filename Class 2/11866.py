import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = [(i+1) for i in range(n)]
res_lst = []

i = k-1
while True:
    res_lst.append(str(lst.pop(i)))
    i += (k-1)
    # print(lst)
    if (len(lst) == 0):
        break
    while (i >= len(lst) and i != 0):
        i -= len(lst)

print('<'+', '.join(res_lst)+'>')