# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# if (n > 54):
#     res = n - 54
# else:
#     res = 1

# while True:
#     cal = res
#     # print("res: ", res)
#     dig = res
#     while (dig != 0):
#         cal += dig % 10
#         dig = dig // 10
#         # print("cal: ", cal)
#     if (cal == n):
#         print(res)
#         break
#     res += 1

n = int(input())

for i in range(1, n+1):
    cal = i
    cal += sum(map(int, str(i)))
    if (cal == n):
        print(i)
        break
    if (i == n):
        print(0)
        break