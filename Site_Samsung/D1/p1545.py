# 거꾸로 출력

import sys
sys.stdin = open("input.txt", "r")

n = int(input())

for i in range (n+1):
    print (n-i, end=" ")