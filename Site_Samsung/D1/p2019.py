# 2를 곱한 값 출력

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
result = 1
for i in range(1, n+2):
    print(result, end=" ")
    result = result * 2
