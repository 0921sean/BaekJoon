# # 노가다
# kg = int(input())

# cnt5 = 0
# cnt5 = kg // 5
# if kg % 5 == 0:
#     cnt3 = 0
#     print(cnt5 + cnt3)
# elif kg % 5 == 1:
#     if cnt5 == 0:
#         print(-1)
#     else:
#         cnt5 -= 1
#         cnt3 = 2
#         print(cnt5 + cnt3)
# elif kg % 5 == 2:
#     if cnt5 == 0 or cnt5 == 1:
#         print(-1)
#     else:
#         cnt5 -= 2
#         cnt3 = 4
#         print(cnt5 + cnt3)
# elif kg % 5 == 3:
#     cnt3 = 1
#     print(cnt5 + cnt3)
# else:
#     if cnt5 == 0:
#         print(-1)
#     else:
#         cnt5 -= 1
#         cnt3 = 3
#         print(cnt5 + cnt3)


# 입력 받기
N = int(input()) # 설탕
res = 0 # 봉지

while N >= 0:
    if N % 5 == 0:
        res += (N // 5)
        print(res)
        break
    # 5로 나눠지지 않았을 때
    N -= 3
    res += 1 # 3kg 봉지 하나 추가
else: # while문에서 else가 나왔을 때
    print(-1)