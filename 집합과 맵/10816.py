# 해쉬 알고리즘
# 입력 받기
N = int(input())
N_lst = list(map(int, input().split()))
dct = {}

# {'카드의 숫자': '숫자의 개수'}로 이루어진 dict 만듦
for i in N_lst:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

M = int(input())
M_lst = list(map(int, input().split()))

for i in M_lst:
    if i in dct: # 주어진 수의 숫자 카드가 존재하는 경우
        print(dct[i], end=" ")
    else: # 존재하지 않는 경우
        print("0", end=" ")

# 문제에서는 이분 탐색으로도 풀 수 있다고 하지만 억지인 것 같음