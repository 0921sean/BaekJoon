import sys
input = sys.stdin.readline

n = int(input())
# value를 2개 준다고 해서 반드시 dict로 표현하려 하지 않기
# dict로 표현하는 것보다 tuple로 표현하는 게 쉬울 수 있다
mem_lst = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    mem_lst.append((age, name))

# 정렬을 쉽게 할 수 있는 장점이 있다
mem_lst.sort(key = lambda x : x[0])

for i in mem_lst:
    sys.stdout.write("{} {}\n".format(i[0], str(i[1])))