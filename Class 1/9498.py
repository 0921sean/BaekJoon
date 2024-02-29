import sys
input = sys.stdin.readline

sco = int(input().rstrip())

if (sco >= 90 and sco <= 100):
    print("A")
elif (sco >= 80):
    print("B")
elif (sco >= 70):
    print("C")
elif (sco >= 60):
    print("D")
else:
    print("F")