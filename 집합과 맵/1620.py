import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split()) # 도감에 있는 포켓몬 수, 맞춰야 하는 문제 수
dct = {} # dict

# {'포켓몬 번호': '포켓몬 이름', '포켓몬 이름': '포켓몬 번호'} 형식의 dict 생성
for i in range(N): # i: 포켓몬 번호
    name = input().rstrip() # name: 포켓몬 이름
    dct[i] = name
    dct[name] = i

for _ in range(M):
    que = input().rstrip() # 문제
    if que.isdigit(): # 문자가 들어왔으면
        print(dct[int(que)-1]) # 포켓몬 번호 출력
    else: # 숫자가 들어왔으면
        print(dct[que]+1) # 포켓몬 이름 출력