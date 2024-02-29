import sys

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

sort_lst = sorted(list(set(lst)))

# for loop에서 index를 매번 구하는 것은 비효율적이다
# list를 dict로 옮겨 index를 구할 수 있게 다른 방법을 생각할 수 있다
num_dict = {sort_lst[i] : i for i in range(len(sort_lst))}

for i in lst:
    sys.stdout.write("{} ". format(str(num_dict[i])))