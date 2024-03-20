# import sys
# input = sys.stdin.readline

# # 입력 받기
# T = int(input().rstrip())

# for _ in range(T):
#     ps = input().rstrip() # 괄호 문자열
#     i = 1
#     while (i != len(ps) and len(ps) != 0):
#         if (ps[0] == ')'):
#             break
#         if (ps[i] == ')'):
#             ps.pop(i)
#             ps.pop(i-1)
#             i = 1
#         else:
#             i += 1
#     if (len(ps) == 0):
#         print("YES")
#     else:
#         print("NO")

import sys
input = sys.stdin.readline

# 입력 받기
T = int(input().rstrip()) # 입력 데이터 수

for _ in range(T):
    ps = input().rstrip() # 괄호 문자열
    stack = [] # 스택
    isValid = True # 바르게 구성된 문자열인지
    for p in ps:
        if p == '(':
            stack.append(p)
        else: # p == ')'
            if (len(stack) != 0 and stack[-1] == '('):
                stack.pop()
            else:
                isValid = False
                break
    if (len(stack) != 0 or not isValid):
        print("NO")
    else:
        print("YES")