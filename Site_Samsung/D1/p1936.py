# 간단한 가위바위보

import sys
sys.stdin = open("input.txt", "r")

a, b = map(int, input().split())

# 가위 1, 바위 2, 보 3

if a == 1:
    if b == 2:
        print("B")
    else:
        print("A")
elif a == 2:
    if b == 1:
        print("A")
    else:
        print("B")
else:
    if b == 1:
        print("B")
    elif b == 2:
        print("A")