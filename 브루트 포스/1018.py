# # 함수를 따로 빼서 정리한 방법
# # 몇 개의 정사각형이 다시 칠해져야 하는지 출력하는 함수
# def check_matrix(mat, i, j):
#     cnt = 0
#     for r in range(i, i+8):
#         for c in range(j, j+8):
#             if ((r+c) % 2 == 0):
#                 if (mat[r][c] != 'W'):
#                     cnt += 1
#             else:
#                 if (mat[r][c] != 'B'):
#                     cnt += 1
#     return min(cnt, 64-cnt)

# import sys
# input = sys.stdin.readline

# # 입력 받기
# N, M = map(int, input().split())

# # 보드 2차원 배열로 만들기
# # ex. board = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', ...]
# board = []
# for _ in range(N):
#     board.append(input().rstrip())

# res = []
# for r in range(N-8+1):
#     for c in range(M-8+1):
#         res.append(check_matrix(board, r, c))

# print(min(res))

import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
res = []

# 보드 2차원 배열로 만들기
# ex. board = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', ...]
board = []
for _ in range(N):
    board.append(input().rstrip())

# (i, j)를 기준으로 8*8 배열에 대해
for i in range(N-8+1):
    for j in range(M-8+1):
        # 다시 칠해야 하는 정사각형의 최소 개수
        cnt = 0
        for r in range(i, i+8):
            for c in range(j, j+8):
                if ((r+c) % 2 == 0):
                    if (board[r][c] != 'W'):
                        cnt += 1
                else:
                    if (board[r][c] != 'B'):
                        cnt += 1
        # 왼쪽 상단이 W인 체스판을 기준으로 개수를 셌으므로 왼쪽 상단이 B인 체스판아 기준일 때랑 비교해야 함
        res.append(min(cnt, 64-cnt))

print(min(res))