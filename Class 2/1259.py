import sys
input = sys.stdin.readline

while True:
    num = input().rstrip()
    if num == "0":
        break
    else:
        if num == num[::-1]:
            print("yes")
        else:
            print("no")