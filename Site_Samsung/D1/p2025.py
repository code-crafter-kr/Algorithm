# N줄 덧셈

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
result = 0
for i in range (0, n+1):
    result += i
print(result)