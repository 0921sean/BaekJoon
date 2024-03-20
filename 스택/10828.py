import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().rstrip()) # 명령의 수
stack = [] # 스택

for _ in range(N):
    com = input().rstrip() # 명령
    l = len(stack)
    # push X
    if com.split()[0] == 'push':
        stack.append(com.split()[1])
    # pop
    elif com == 'pop':
        if l == 0:
            print("-1")
        else:
            print(stack.pop())
    # size
    elif com == 'size':
        print(l)
    # empty
    elif com == 'empty':
        if l == 0:
            print(1)
        else:
            print(0)
    # top
    elif com == 'top':
        if l == 0:
            print("-1")
        else:
            print(stack[-1])