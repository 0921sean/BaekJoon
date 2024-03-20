T = int(input())
list = []

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    ho = (N // H) + 1
    if (floor == 0):
        floor = H
        ho = N // H
    list.append(floor * 100 + ho)

for i in list:
    print(i)