# 문자열 대문자 변환

import sys
sys.stdin = open("input.txt", "r")


n = input()

for i in n:
    print(i.upper(), end="")