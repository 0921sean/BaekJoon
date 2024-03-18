# # 규칙성 활용
# import sys
# input = sys.stdin.readline

# # 입력 받기
# N, K = map(int, input().split())

# # ex. N = 7 -> queue = [1, 2, 3, 4, 5, 6, 7]
# queue = [(i+1) for i in range(N)]
# res = []

# i = 0
# while queue:
#     i += (K-1)
#     while (i >= len(queue)):
#         i -= len(queue)
#     res.append(str(queue.pop(i)))

# # 결과 출력
# print('<' + ', '.join(res) + '>')

# deque 활용
from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().split())

deq = deque([(i+1) for i in range(N)])
res = []

while deq:
    # K-1번째 노드까지 deq 맨 뒤로 이동시킴
    for _ in range(K-1):
        deq.append(deq.popleft())
    # K번째 노드 삭제 후 res에 추가
    res.append(str(deq.popleft()))

# 결과 출력
print('<' + ', '.join(res) + '>')