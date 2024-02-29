import sys
input = sys.stdin.readline

lst = []
n = int(input().rstrip())

for _ in range(n):
    com = input().rstrip()
    if (com.split()[0] == 'push'):
        lst.append(com.split()[1])
    elif (com == 'pop'):
        l = len(lst)
        if (l == 0):
            print("-1")
        else:
            print(lst.pop(0))
    elif (com == 'size'):
        print(len(lst))
    elif (com == 'empty'):
        if (len(lst) == 0):
            print(1)
        else:
            print(0)
    elif (com == 'front'):
        if (len(lst) == 0):
            print("-1")
        else:
            print(lst[0])
    elif (com == 'back'):
        l = len(lst)
        if (l == 0):
            print("-1")
        else:
            print(lst[l-1])