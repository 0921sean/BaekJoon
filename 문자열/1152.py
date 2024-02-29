string = str(input())

cnt = len(string.split(' '))
if string[0] == ' ':
    cnt -= 1
if string[-1] == ' ':
    cnt -= 1
print(cnt)