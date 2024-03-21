import sys
input = sys.stdin.readline

# 입력 받기
N, M, B = map(int, input().split()) # 집터의 세로 길이, 가로 길이, 인벤토리에 있는 블록의 개수
h_dct = {h : 0 for h in range(257)} # 현재 땅의 높이 각각의 개수

# {'땅의 높이': '개수}를 dict 형태로
for _ in range(N):
    temp = list(map(int, input().split()))
    for h in temp:
        h_dct[h] += 1

h_dct = list(h_dct.items()) # for문에 사용하기 위해 타입 변경
time_lst = [] # 걸리는 시간 리스트

for i in range(257):
    over = [(k, v) for k, v in h_dct if k > i and v != 0] # 현재 높이(k)가 원하는 높이(i)보다 높은 경우
    under = [(k, v) for k, v in h_dct if k < i and v != 0] # 현재 높이(k)가 원하는 높이(i)보다 낮은 경우
    time = 0 # 걸리는 시간
    block = B # 남은 인벤토리 블록 개수

    for h, cnt in over: # 높은 경우에 대해 계산
        time += 2 * (h - i) * cnt
        block += (h - i) * cnt
    for h, cnt in under: # 낮은 경우에 대해 계산
        time += (i - h) * cnt
        block -= (i - h) * cnt

    if block < 0: # 원하는 높이(i)를 구현할 수 없는 경우
        break # time_lst에 추가하지 않음
    time_lst.append(time) # break를 거치지 않은 경우 추가

min_time = min(time_lst) # 걸리는 시간 중 최솟값
idx_lst = [idx for idx, t in enumerate(time_lst) if t == min_time] # 최소 걸리는 시간의 인덱스들 리스트
max_idx = max(idx_lst) # 인덱스들 중 최댓값

# 결과 출력하기
print(min_time, max_idx)