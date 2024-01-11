import sys
sys.stdin = open("input.txt", "r")

n = int (input())

list_A = [input().split() for _ in range(n)]

for i in range (n):
    list_A[i][0], list_A[i][1] = list_A[i][1], list_A[i][0]
    list_A[i][0] = int(list_A[i][0])

list_A.sort()
list_A.reverse()
print(list_A[2][1])