# 자릿수 합 구하기
import sys
sys.stdin = open("input.txt", "r")

n  = input()
sum = 0
for i in n:
    sum += int(i)
print(sum)