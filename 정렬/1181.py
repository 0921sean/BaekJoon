import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 단어의 개수

lst = []
for _ in range(N):
    lst.append(input().rstrip()) # 단어들을 list로 받음

lst = sorted(set(lst)) # 중복된 단어 처리, 사전 순 정렬
lst.sort(key=len) # 길이 짧은 순 정렬

for i in lst:
    print(i)