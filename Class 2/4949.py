# 첫번째 시도
# import sys
# input = sys.stdin.readline

# while True:
#     sen = input().rstrip()
#     par = ''
#     temp = True

#     if (sen == '.'):
#         break
#     for i in sen:
#         if (i in ['(', ')', '[', ']']):
#             par += i
#         if (i == '.'):
#             break
    
#     while True:
#         f = True
#         if (par.find('()') != -1):
#             f = False
#             par.replace('()', '')
#         if (par.find('[]') != -1):
#             f = False
#             par.replace('[]', '')
#         if f:
#             print(f)
#             if (par == ''):
#                 print("yes")
#                 temp = False
#                 break
#     if temp:
#         print("no")

import sys
input = sys.stdin.readline

while True:
    sen = input().rstrip()
    stack = []
    temp = False

    if (sen == '.'):
        break
    for s in sen:
        if (s == '(' or s == '['):
            stack.append(s)
        elif s == ')':
            if (len(stack) != 0 and stack[-1] == '('):
                stack.pop()
            else:
                temp = True
                break
        elif s == ']':
            if (len(stack) != 0 and stack[-1] == '['):
                stack.pop()
            else:
                temp = True
                break
    if (len(stack) != 0 or temp):
        print("no")
    else:
        print("yes")