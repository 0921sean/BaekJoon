from collections import deque
import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 명령의 수
deq = deque()

for _ in range(N):
    com = input().rstrip() # 명령
    l = len(deq) # 덱에 들어있는 정수의 개수
    # push_front X
    if com.split()[0] == 'push_front':
        deq.append(0) # 덱 가장 뒤에 0을 임의로 추가
        for i in range(l, 0, -1):
            deq[i] = deq[i-1] # 덱의 정수들을 한 칸씩 뒤로 밀음
        deq[0] = com.split()[1] # 그 후 덱 가장 앞의 숫자를 정수 X로 덮음
    # push_back X
    elif com.split()[0] == 'push_back':
        deq.append(com.split()[1])
    # pop_front
    elif com == 'pop_front':
        if l == 0:
            print("-1")
        else:
            print(deq.popleft())
    # pop_back
    elif com == 'pop_back':
        if l == 0:
            print("-1")
        else:
            print(deq.pop())
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
    elif com == 'back':
        if l == 0:
            print("-1")
        else:
            print(deq[-1])