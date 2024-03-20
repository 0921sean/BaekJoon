# 개수 세기와 출력값을 위해 upper함
word = str(input()).upper()
alpha_dict = {}

# dict 형태로 알파벳, 개수를 각각 key, value로 저장
for alpha in word:
    if alpha not in alpha_dict.keys():
        alpha_dict[alpha] = 1
    else:
        alpha_dict[alpha] += 1

# 최대 개수의 알파벳이 몇 개인지 cnt에 저장
max = max(alpha_dict.values())
cnt = 0
for val in alpha_dict.values():
    if val == max:
        cnt += 1

# 최대 개수의 알파벳이 한 개라면 index를 출력, 그 외의 경우에는 '?' 출력
if cnt == 1:
    max_index = list(alpha_dict.values()).index(max)
    print(list(alpha_dict.keys())[max_index])
else:
    print('?')