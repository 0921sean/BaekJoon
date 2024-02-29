# 문제에서 내장 함수 사용을 추천한다고 함
# sorted 사용
import sys
n = int(input())
lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

for i in sorted(lst):
    sys.stdout.write(str(i)+'\n')