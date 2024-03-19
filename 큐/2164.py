# Queue 사용
from collections import deque

# 입력 받기
N = int(input())

deq = deque([(i+1) for i in range(N)])
l = len(deq)

for _ in range(l-1):
    # 제일 위 카드 버리기
    deq.popleft()

    # 위 카드 제일 아래로 옮기기
    num = deq.popleft()
    deq.append(num)

# 결과 출력하기
print(deq[0])

# # 규칙 발견해서 사용
# # n = 1 -> output = 1 = (1-0)
# # n = 2 -> output = 2 = (2-1)*2
# # n = 3 -> output = 2 = (3-2)*2
# # n = 4 -> output = 4 = (4-2)*2
# # n = 5 -> output = 2 = (5-4)*2
# # n = 6 -> output = 4 = (6-4)*2
# # n = 7 -> output = 6 = (7-4)*2
# # n = 8 -> output = 8 = (8-4)*2

# N = int(input())
# i = 1

# if (N == 1):
#     print(1)
# else:
#     while (i < N):
#         i *= 2
#     i = i // 2
#     print((N - i) * 2)