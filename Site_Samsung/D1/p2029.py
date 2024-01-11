# 몫과 나머지 출력

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
for i in range (n):
    a, b = map(int, input().split())
    print(f'#{i+1} {a//b} {a%b}')