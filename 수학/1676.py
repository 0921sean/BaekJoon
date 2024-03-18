N = int(input())

num = 1
cnt = 0

while (N != 0): # while문이 완료되면 num = N!
    num *= N
    N -= 1

while True:
    if (num % 10 == 0): # 뒤에서부터 0의 개수를 cnt로 셈
        cnt += 1
    else:
        break
    num = num // 10

print(cnt)