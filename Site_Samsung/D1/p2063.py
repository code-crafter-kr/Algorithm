# 중간값 구하기

import sys
sys.stdin = open("input.txt", "r")

n = int(input())

lst = list(map(int, input().split()))
lst.sort()
print(lst[len(lst)//2])