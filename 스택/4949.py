import sys
input = sys.stdin.readline

while True:
    # 입력 받기
    sen = input().rstrip() # 문자열
    stack = []
    isBal = True # 균형을 이루고 있는지 여부

    if (sen == '.'): # 입력 종료조건
        break
    for s in sen:
        if (s == '(' or s == '['):
            stack.append(s)
        elif s == ')':
            if (len(stack) != 0 and stack[-1] == '('):
                stack.pop()
            else:
                isBal = False
                break
        elif s == ']':
            if (len(stack) != 0 and stack[-1] == '['):
                stack.pop()
            else:
                isBal = False
                break
        # else는 영문 알파벳, 공백일 때다
    if (len(stack) != 0 or not isBal):
        print("no")
    else:
        print("yes")