import sys
sys.stdin = open("input.txt", "r")


m, n = map(int, input().split())

lst1 = []
lst2 = []
for i in range (m):
    temp = list(map(int, input().split()))
    lst1.append(temp)

for j in range (m):
    temp = list(map(int, input().split()))
    for x in range (n):
        lst1[j][x] += temp[x]

for i in lst1:
    print(*i)
