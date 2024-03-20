# from collections import deque
# import sys
# input = sys.stdin.readline

# test_num = int(input().rstrip())

# for _ in range(test_num):
#     cnt = 0
#     i = 0
#     n, m = map(int, input().split())
#     queue = deque(list(map(int, input().split())))

#     while True:
#         max_num = max(queue)
#         print(max_num)
#         max_ind = queue.index(max_num)
#         print(max_ind)
#         if (max_ind == m):
#             cnt += 1
#             break
#         for _ in range(max_ind):
#             num = queue.popleft()
#             queue.append(num)
#         queue.popleft()
#         cnt += 1
#         m = m + n - max_ind - 1
#     print(cnt)

from collections import deque
import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0

    while queue:
        max_num = max(queue)
        front = queue.popleft()
        m -= 1

        if (max_num == front):
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1