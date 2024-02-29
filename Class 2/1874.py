# import sys
# input = sys.stdin.readline

# cnt = 0
# stack = []
# op = []
# temp = True
# n = int(input().rstrip())
# lst = [(i+1) for i in range(n)]

# for i in range(n):
#     num = int(input().rstrip())
#     while (cnt < num):
#         fir = lst[0]
#         stack.append(fir)
#         lst.remove(fir)
#         op.append("+")
#         cnt = fir
#     if (stack[-1] == num):
#         stack.pop()
#         op.append("-")
#         cnt = num
#     else:
#         temp = False

# if temp == False:
#     print("NO")
# else:
#     for i in op:
#         print(i)

# cnt를 더 효율적으로 사용
import sys
input = sys.stdin.readline

cnt = 1
temp = True
stack = []
op = []

n = int(input().rstrip())
for i in range(n):
    num = int(input().rstrip())
    while cnt <= num:
        stack.append(cnt)
        op.append("+")
        cnt += 1
    
    if (stack[-1] == num):
        stack.pop()
        op.append("-")
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in op:
        print(i)