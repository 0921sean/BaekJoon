print_list = []

num = 0
while True:
    list = []
    num = int(input())
    if num == -1:
        break
    for x in range(1, num):
        if num % x == 0:
            list.append(x)

    if num == sum(list):
        res = ("{} = ".format(num))
        for elem in list[:-1]:
            res += ("{} + ".format(elem))
        res += ("{}".format(list[-1]))
        print_list.append(res)
    else:
        print_list.append("{} is NOT perfect.".format(num))

for i in print_list:
    print(i)