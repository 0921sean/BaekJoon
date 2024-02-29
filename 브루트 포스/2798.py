N, M = map(int, input().split())
card_num = list(map(int, input().split()))
list = []
pos_list = []

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = card_num[i] + card_num[j] + card_num[k]
            list.append(M - sum)

for l in list:
    if l >= 0:
        pos_list.append(l)
print(M - min(pos_list))