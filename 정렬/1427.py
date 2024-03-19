num = int(input())
lst = []
res = 0

while (num != 0):
    d = num % 10
    lst.append(d)
    num = num // 10

sort_lst = sorted(lst, reverse=True)

for i in sort_lst:
    res *= 10
    res += i

print(res)