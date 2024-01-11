import sys

sys.stdin = open("input.txt", "r")

m, n = map(int, input().split())
lst = [0 for _ in range (m)]

for i in range (n):
    a, b, c = map(int, input().split())
    for j in range (a-1, b):
        lst[j] = c

print(*lst)