# 시간 초과
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())

# lst = [(i+1) for i in range(n)]
# l = len(lst)

# for _ in range(2, l):
#     lst.remove(lst[0])
#     num = lst[0]
#     lst.remove(num)
#     lst.append(num)
# lst.remove(lst[0])

# print(lst[0])

# 특별한 규칙이 있음을 유추(이 코드는 틀림)
# import sys
# input = sys.stdin.readline

# i = 1
# n = int(input().rstrip())

# while (i <= n):
#     i *= 2

# print(i // 2)

# Queue 사용
from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())

deque = deque([(i+1) for i in range(n)])
l = len(deque)

for _ in range(1, l):
    deque.popleft()
    num = deque.popleft()
    deque.append(num)

print(deque[0])

# 규칙 발견
# n = 1 -> output = 1 = (1-0)
# n = 2 -> output = 2 = (2-1)*2
# n = 3 -> output = 2 = (3-2)*2
# n = 4 -> output = 4 = (4-2)*2
# n = 5 -> output = 2 = (5-4)*2
# n = 6 -> output = 4 = (6-4)*2
# n = 7 -> output = 6 = (7-4)*2
# n = 8 -> output = 8 = (8-4)*2
# import sys
# input = sys.stdin.readline

# i = 1
# n = int(input().rstrip())

# if (n == 1):
#     print(1)
# else:
#     while (i < n):
#         i *= 2
#     i = i // 2
#     print((n - i) * 2)