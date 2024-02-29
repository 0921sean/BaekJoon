kg = int(input())

cnt5 = 0
cnt5 = kg // 5
if kg % 5 == 0:
    cnt3 = 0
    print(cnt5 + cnt3)
elif kg % 5 == 1:
    if cnt5 == 0:
        print(-1)
    else:
        cnt5 -= 1
        cnt3 = 2
        print(cnt5 + cnt3)
elif kg % 5 == 2:
    if cnt5 == 0 or cnt5 == 1:
        print(-1)
    else:
        cnt5 -= 2
        cnt3 = 4
        print(cnt5 + cnt3)
elif kg % 5 == 3:
    cnt3 = 1
    print(cnt5 + cnt3)
else:
    if cnt5 == 0:
        print(-1)
    else:
        cnt5 -= 1
        cnt3 = 3
        print(cnt5 + cnt3)