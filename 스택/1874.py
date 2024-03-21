import sys
input = sys.stdin.readline

# 입력 받기
n = int(input().rstrip()) # 1~n 정수
stack = [] # 스택
op = [] # 필요한 연산
cnt = 1 # 1~n 정수 중 무슨 숫자까지 사용되었는지 
isAble = True # 입력된 수열을 만들 수 있는지 여부

for i in range(n):
    num = int(input().rstrip()) # 주어진 정수
    while cnt <= num:
        stack.append(cnt)
        op.append("+")
        cnt += 1
    
    if (stack[-1] == num):
        stack.pop()
        op.append("-")
    else:
        isAble = False
        break

if isAble == False:
    print("NO")
else:
    for i in op:
        print(i)