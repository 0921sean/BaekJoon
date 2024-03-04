import sys
input = sys.stdin.readline

m = int(input().rstrip())
S = set()

for _ in range(m):
    sen = input().rstrip()
    cmd = sen.split()[0]
    if cmd == 'all':
        S = ({(i+1) for i in range(20)})
        # S = set([(i+1) for i in range(20)])
    elif cmd == 'empty':
        S.clear()
    else:
        num = int(sen.split()[1])
        
        if cmd == 'add':
            S.add(num)
        elif cmd == 'remove':
            S.discard(num)
        elif cmd == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)
    # print(S)
                
