import sys
input = sys.stdin.readline

lst = []
n = int(input().rstrip())

for _ in range(n):
    com = input().rstrip()
    if (com.split()[0] == 'push_front'):
        l = len(lst)
        lst.append(0)
        for i in range(l, 0, -1):
            lst[i] = lst[i-1]
        lst[0] = com.split()[1]
    elif (com.split()[0] == 'push_back'):
        lst.append(com.split()[1])
    elif (com == 'pop_front'):
        if (len(lst) == 0):
            print("-1")
        else:
            print(lst.pop(0))
    elif (com == 'pop_back'):
        l = len(lst)
        if (l == 0):
            print("-1")
        else:
            print(lst.pop(l-1))
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