N = int(input())

num = 666
cnt = 0
while True:
    num = str(num)
    if (num.find('666') != -1):
        cnt += 1
    if cnt == N:
        break
    num = int(num) + 1
print(num)