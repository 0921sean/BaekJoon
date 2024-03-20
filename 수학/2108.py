import sys
input = sys.stdin.readline

lst = []
dct = {}
dct_cnt = 0
n = int(input().rstrip())

for _ in range(n):
    num = int(input().rstrip())
    lst.append(num)
    if num in dct:
        dct[num] += 1
    else:
        dct[num] = 1
        dct_cnt += 1

# 만약 시간초과가 났다면, 산술평균과 최빈값의 공통 부분을 합치는 게 좋아보임
# 산술평균
tot = 0
for k, v in dct.items():
    tot += k * v
print(round(tot/n))

# 중앙값
sort_lst = sorted(lst)
print(sort_lst[n//2])

# 최빈값
fre_lst = []
fre_cnt = 0
max_num = max(dct.values())
for k, v in dct.items():
    if (v == max_num):
        fre_lst.append(k)
        fre_cnt += 1
fre_lst.sort()
if fre_cnt > 1:
    print(fre_lst[1])
else:
    print(fre_lst[0])

# 범위
print(sort_lst[n-1] - sort_lst[0])