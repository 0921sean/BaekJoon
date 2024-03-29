import sys
input = sys.stdin.readline

# 입력 받기
t = int(input().rstrip()) # 테스트 케이스 수

for _ in range(t):
    n = int(input().rstrip()) # 의상 수
    dct = {}
    for _ in range(n):
        # ex. dct = {'headgear': 2, 'eyewear': 1}
        name, type = input().split() # 의상 이름, 종류
        if type in dct:
            dct[type] += 1
        else:
            dct[type] = 1
        
    res = 1
    for k, v in dct.items():
        res *= (1+v)
    res -= 1
    
    # 결과 출력하기
    print(res)