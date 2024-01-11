import sys
sys.stdin = open("input.txt" , "r")

N = int(sys.stdin.readline())
list_A = list(map(int, sys.stdin.readline().split()))
list_B = sorted(set(list_A))

list_X = [[] for _ in range (min(list_A), (max(list_A)+1))]

if min(list_A) < 0:
    list_X = [[] for _ in range (min(list_A), (max(list_A)+1))]

    for i in range (len(list_B)):
        list_X[list_B[i]-min(list_A)].append(i)

    for i in list_A:
        print(list_X[i-min(list_A)][0], end = " ")

else:
    list_X = [[] for _ in range (0,max(list_A)+1)]

    for i in range (len(list_B)):
        list_X[list_B[i]].append(i)

    for i in list_A:
        print(list_X[i][0], end = " ")
