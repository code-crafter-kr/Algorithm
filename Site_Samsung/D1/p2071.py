# 평균값 구하기
import sys
sys.stdin = open("input.txt", "r")

n = int(input())

for i in range (n):
    result = 0
    lst = list(map(int, input().split()))
    for a in lst:
        result += a
    result = round(result / len(lst))
    print(f'#{i+1} {result}')