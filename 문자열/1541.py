# 입력 받기
cal = input() # 연산식
cal += '+' # 마지막 num까지 더해주기 위해 맨 뒤에 연산자 추가
res = 0 # 결과

num = 0 # 연산식의 숫자
isSub = False # 빼기가 적용되는지 여부
for i in cal:
    if i.isdigit(): # 숫자라면
        if num != 0:
            num *= 10
        num += int(i) # num 값에 축적
    else: # 연산자라면
        if isSub:
            res -= num
        else:
            res += num # 빼기 적용되는지 여부에 따라 결과에 연산
        num = 0
        if i == '-':
            isSub = True

# 결과 출력하기
print(res)