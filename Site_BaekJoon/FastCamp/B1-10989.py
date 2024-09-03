import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

list_A = [0 for i in range (0, 10001)]

N = int(input())

for _ in range (N):
    a = int(input())
    list_A[a-1] += 1

j = 1
for i in (list_A):
    for x in range (i):
        print(j)
    j = j + 1