import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().rstrip()) # 수의 개수
lst = [] # 중앙값, 범위를 위함
dct = {} # 산술평균, 최빈값을 위함

# 정렬된 리스트 생성
for _ in range(N):
    lst.append(int(input().rstrip()))
lst.sort() # 정렬 (어차피 lst는 중앙값, 범위에서만 사용하며 둘 다 정렬된 리스트를 필요로 함)

# {'정수': '개수'}로 dict 생성 (최빈값을 쉽게 구하기 위해 key가 정렬된 dict를 만듦)
for i in lst:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

# 산술평균
tot = 0
for k, v in dct.items():
    tot += k * v
print(round(tot / N))

# 중앙값
print(lst[N//2])

# 최빈값
max_fre = max(dct.values()) # 최대빈도수
res = 0 # 최빈값
cnt = 0 # 최빈값의 개수

for k, v in dct.items():
    if v == max_fre: # 해당 정수가 최빈값이라면
        res = k # res를 업데이트하고
        cnt += 1 # 최빈값의 개수를 하나 더함
    if cnt == 2: # 최빈값의 개수가 2개면
        break # 방금 업데이트한 res가 최빈값 중 두 번째로 작은 값이므로 반복문 나감
print(res)

# 범위
print(lst[-1] - lst[0])