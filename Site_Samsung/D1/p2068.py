# 최대수 구하기
import sys
sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    result = -1
    lst = list(map(int, input().split()))
    for a in lst:
        result = max(result, a)
    print(f'#{i+1} {result}')