import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dct = {}

for _ in range(N):
    url, pw = input().split()
    dct[url] = pw

for _ in range(M):
    find_url = input().rstrip()
    print(dct[find_url])