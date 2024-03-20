# res = 1 => input = 1 (1개)
# res = 2 => input = 2 ~ 7 (6개) (6*0+2 ~ 6*0+2+6*1)
# res = 3 => input = 8 ~ 19 (12개) (6*1+2 ~ 6*1+2+6*2)
# res = 4 => input = 20 ~ 37 (18개)
# res = 5 => input = 38 ~ 61 (24개)

n = int(input())
i = 2

while True:
    if n == 1:
        print(1)
        break
    if (n <= 3*i*(i-1)+1):
        print(i)
        break
    i += 1