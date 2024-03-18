import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = []

# ex. lst = [(21, 'Junkyu'), (21, 'Dohyun'), (20, 'Sunyoung')]
for i in range(N):
    age, name = input().split()
    age = int(age)
    lst.append((age, name))

# 특정 변수(여기서는 age)를 기준으로만 해서 정렬할 수 있음
lst.sort(key = lambda x : x[0])

for i in lst:
    print("{} {}".format(i[0], i[1]))