import sys
sys.stdin = open("input.txt", "r")

lst = [[0 for i in range (100)] for j in range (100)]

n = int(input())

for i in range (n):
    n, m = map(int, input().split())
    for x in range (n, n + 10):
        for y in range (m, m + 10):
            lst[x][y] = 1

result = 0
for i in lst:
    result += i.count(1)
print(result)

