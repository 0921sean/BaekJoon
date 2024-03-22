import sys
input = sys.stdin.readline

# 입력 받기
M = int(input().rstrip()) # 연산의 수
S = set() # 집합

for _ in range(M):
    sen = input().rstrip() # 연산
    cmd = sen.split()[0] # 명령어
    # all
    if cmd == 'all':
        S = ({(i+1) for i in range(20)})
    # empty
    elif cmd == 'empty':
        S.clear()
    else:
        x = int(sen.split()[1]) # 숫자
        
        # add x
        if cmd == 'add':
            S.add(x)
        # remove x
        elif cmd == 'remove':
            S.discard(x) # 있으면 제거, 없으면 연산 무시
        # check x
        elif cmd == 'check':
            if x in S: # x 있으면 1 출력
                print(1)
            else: # 없으면 0 출력
                print(0)
        # toggle x
        elif cmd == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)