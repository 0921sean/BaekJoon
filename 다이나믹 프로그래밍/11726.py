# 입력 받기
n = int(input()) # 2*n 크기의 직사각형
lst = [0, 1, 2]

# 피보나치 수열 리스트(길이 1001) 생성
for _ in range(998):
    lst.append(lst[-1]+lst[-2])

# 결과 출력하기
print(lst[n] % 10007)