# 단어를 입력받고 전체 글자수를 cnt에 저장
word = str(input())
cnt = len(word)

# 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='의 개수를 세서 2글자 -> 1글자로 수정 
# 'dz='의 개수를 세서 3글자 -> 1글자로 수정 (이미 위에서 'z=' 개수로 하나 감소됨)
cro_list = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
for cro in cro_list:
    cnt -= word.count(cro)
cnt -= word.count('dz=')
print(cnt)