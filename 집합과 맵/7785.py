# set 사용
# import sys
# input = sys.stdin.readline

# s = set()

# n = int(input().rstrip())

# for i in range(n):
#     name, el = input().split()
#     if el == 'enter':
#         s.add(name)
#     else:
#         s.discard(name)

# lst = []
# lst = list(s)
# lst.sort(reverse=True)

# for i in lst:
#     print(i)


# dict 사용
import sys
input = sys.stdin.readline

dct = {}

n = int(input().rstrip())

for _ in range(n):
    name, el = input().rstrip().split()
    if el == 'enter':
        dct[name] = True
    else:
        del dct[name]

print('\n'.join(sorted(dct.keys(), reverse=True)))