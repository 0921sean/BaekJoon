# check how many elements should change in 8*8 matrix
def check_matrix(mat, i, j):
    cnt = 0
    for r in range(i, i+8):
        for c in range(j, j+8):
            if ((r+c) % 2 == 0):
                if (mat[r][c] != 'W'):
                    cnt += 1
            else:
                if (mat[r][c] != 'B'):
                    cnt += 1
    return min(cnt, 64-cnt)

N, M = map(int, input().split())

# matrix is 2d array
matrix = []
for _ in range(N):
    row = []
    elements = input()
    for el in elements:
        row.append(el)
    matrix.append(row)

list = []
for r in range(0, N-8+1):
    for c in range(0, M-8+1):
        list.append(check_matrix(matrix, r, c))

print(min(list))