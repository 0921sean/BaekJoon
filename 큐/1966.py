from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
T = int(input().rstrip()) # 테스트케이스 수

for _ in range(T):
    N, M = map(int, input().split()) # 문서 개수, 궁금한 문서가 몇 번째에 놓여 있는지
    deq = deque(list(map(int, input().split()))) # 큐
    res = 0 # 문서가 몇 번쨰로 인쇄되는지

    while deq:
        max_num = max(deq)
        front = deq.popleft()
        M -= 1

        if (max_num == front):
            res += 1
            if M < 0:
                print(res)
                break
        else:
            deq.append(front) # 문서를 인쇄하지 않고 큐의 가장 뒤에 재배치
            if M < 0:
                M = len(deq) - 1