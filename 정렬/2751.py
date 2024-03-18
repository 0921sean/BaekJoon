import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = []

for _ in range(N):
    lst.append(int(input().rstrip())) # N개의 수를 list로 받음

for i in sorted(lst): # 정렬함과 동시에 출력
    print(i)