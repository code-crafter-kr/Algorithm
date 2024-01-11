import sys
sys.stdin=open('input.txt','r')

n = int(input())
list_A =[]

for i in range (n):
    list_A.append(list(map(int,(input().split()))))
    list_A[i][0], list_A[i][1] = list_A[i][1], list_A[i][0]

list_A.sort()

for i in list_A:
    print(i[1], i[0])