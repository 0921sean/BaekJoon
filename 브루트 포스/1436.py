N = int(input())

num = 666 # N 최솟값이 1이므로 666부터 시작
cnt = 0

while True:
    num = str(num) # '666' 문자열이 있는지로 판단하면 쉬우므로 str로 전환
    if (num.find('666') != -1): # '666'이 있다면
        cnt += 1 # cnt로 체크
    if cnt == N:
        break
    num = int(num) + 1

print(num)