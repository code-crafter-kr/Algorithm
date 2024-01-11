# 알파벳 숫자 변환

import sys
sys.stdin = open("input.txt", "r")

n = input()

for i in n:
    x = i.upper()
    print(ord(x)-64, end=" ")