T = int(input())

for _ in range(T):
    S = input()
    sco = 0

    for i in range(len(S)):
        if (S[i] == "O"):
            j = i
            while (S[j] != 'X'):
                sco += 1
                if (j == 0):
                    break
                j -= 1
    print(sco)

    # 아래의 방법으로도 할 수 있을까?
    # for i in range(1, 80):
    #     sco += S.count("O" * i)
    # print(sco)