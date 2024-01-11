import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

list_A = []
for i in range (N):
    list_A.append(sys.stdin.readline().split())
    list_A[i][0] = int(list_A[i][0])
    list_A[i].append(i)
    list_A[i][2], list_A[i][1] = list_A[i][1], list_A[i][2]
list_A.sort()

for i in list_A:
    print(i[0], i[2])