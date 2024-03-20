# 이 단어가 그룹 단어인지를 찾아주는 함수 생성
def check_group(word):
    index = 0
    result = True
    while (index < len(word)-1):
        # 현재 알파벳과 다음 알파벳이 다르면 그 다음부터 현재 알파벳과 겹치는 글자가 있는지 확인
        # 있는 경우 이 단어는 그룹 단어가 아니므로 False를 리턴함
        if word[index] != word[index + 1]:
            split_word = word[index+2: ]
            if split_word.find(word[index]) != -1:
                result = False
                break
        index += 1
    return result

# 입력받을 단어의 개수 N과 단어들을 입력
N = int(input())
words = [str(input()) for _ in range(N)]

# 그룹 단어의 개수를 cnt에 저장하여 리턴 
cnt = 0
for word in words:
    if check_group(word) == True:
        cnt += 1
print(cnt)