import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

lst = [x for x in range(1, n+1)]


for _ in range (m):
    i, j = map(int, input().split())
    temp = lst[i-1]
    lst[i-1] = lst[j-1]
    lst[j-1] = temp
    
print(*lst)
