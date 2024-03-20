from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 명령의 수
deq = deque() # 큐

for _ in range(N):
    com = input().rstrip() # 명령
    l = len(deq) # 큐에 들어있는 정수의 개수
    # push X
    if com.split()[0] == 'push':
        deq.append(com.split()[1])
    # pop
    elif com == 'pop':
        if l == 0:
            print("-1")
        else:
            print(deq.popleft())
    # size
    elif com == 'size':
        print(l)
    # empty
    elif com == 'empty':
        if l == 0:
            print(1)
        else:
            print(0)
    # front
    elif com == 'front':
        if l == 0:
            print("-1")
        else:
            print(deq[0])
    # back
    else: # com == 'back'
        if l == 0:
            print("-1")
        else:
            print(deq[-1])