import sys
sys.stdin = open("input.txt", "r")

a = int(input())
lst = list(map(int, input().split()))
lst.sort()

print(lst[0]*lst[-1])