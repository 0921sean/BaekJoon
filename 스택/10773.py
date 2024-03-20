import sys
input = sys.stdin.readline

# 입력 받기
K = int(input().rstrip()) # 주어지는 정수의 수
stack = [] # 스택

for _ in range(K):
    num = int(input().rstrip()) # 정수
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

# 결과 출력하기
print(sum(stack))