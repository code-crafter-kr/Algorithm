import sys
sys.stdin = open("input.txt", "r")


list_A = [0 for i in range (0, 200)]

N = int(sys.stdin.readline())
list_X = [[] for i in range (0,200)]
for _ in range (N):
    a = sys.stdin.readline().split()
    a[0] = int(a[0])
    list_A[a[0]-1] += 1 #나이에 맞게 카운팅
    list_X[a[0]-1].append(a[1])

j = 1
for i in (list_A):
    for x in range (i):
        print(j, list_X[j-1][x])
    j = j + 1