import sys
sys.stdin = open("input.txt", "r")

list_A = [0 for i in range (0, 10001)]

N = int(sys.stdin.readline())

for _ in range (N):
    a = int(sys.stdin.readline())
    list_A[a-1] += 1

j = 1
for i in (list_A):
    for x in range (i):
        print(j)
    j = j + 1

