import sys
input = sys.stdin.readline

word_set = set()
s = input().rstrip()

n = len(s)

for i in range(n):
    for j in range(i, n):
        word_set.add(s[i:j+1])

print(len(word_set))

