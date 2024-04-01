# 입력 받기
n = int(input()) # 2xn 크기의 직사각형
lst = [0, 1, 3] # 채우는 방법 수 리스트

for _ in range(998):
    lst.append(lst[-1] + lst[-2]*2)

# 결과 출력하기
print(lst[n] % 10007)