import sys


sys.stdin = open("input.txt", "r")

lst = [0] + [1] * 30

for _ in range (28):
    stu = int(input())
    lst[stu] = 0

for x in (i for i in range(31) if lst[i] == 1):
    print(x)
