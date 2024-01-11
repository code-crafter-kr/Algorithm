#대각선 출력하기

import sys
sys.stdin = open("input.txt", "r")

for i in range(5):
    for j in range(5):
        if i == j:
            print("#", end="")
        else:
            print("+", end="")
    print()