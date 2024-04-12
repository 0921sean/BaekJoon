# 입력 받기
cal = input()
cal += '+'
res = 0

num = 0
isSub = False
for i in cal:
    if i.isdigit():
        if num != 0:
            num *= 10
        num += int(i)
    else:
        if isSub:
            res -= num
        else:
            res += num
        num = 0
        if i == '-':
            isSub = True

print(res)