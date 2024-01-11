# 홀수만 더하기
import sys
sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    result = 0
    lst = list(map(int, input().split()))
    for _ in lst:
        if _ % 2 == 1:
            result += _
    print('#{} {}'.format(i+1, result))