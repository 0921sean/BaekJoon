A = int(input())
B = int(input())
C = int(input())
res = str(A * B * C)

for i in range(10):
    cnt = 0
    for j in res:
        if (int(j) == i):
            cnt += 1
    print(cnt)