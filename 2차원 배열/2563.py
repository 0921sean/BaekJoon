arr = [[0 for _ in range(100)] for _ in range(100)]
# 아래의 경우로 arr을 만들면 arr[1][1] = 1을 했을 때 arr[x][1]이 전부 1이 됨
# 이유가 뭘까?
# rows, cols = (100, 100)
# arr = [[0] * cols] * rows

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for a in range(x, x+10):
        for b in range(y, y+10):
            arr[a][b] = 1

count = 0
for x in range(0, 100):
    for y in range(0, 100):
        if arr[x][y] == 1:
            count += 1
print(count)