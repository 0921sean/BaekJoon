import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split()) # 저장된 사이트 주소 수, 비밀번호 찾으려는 사이트 주소 수
dct = {}

# {'사이트 주소': '비밀번호'} dict 생성
for _ in range(N):
    url, pw = input().split() # 사이트 주소, 비밀번호
    dct[url] = pw

# 결과 출력하기
for _ in range(M):
    print(dct[input().rstrip()])