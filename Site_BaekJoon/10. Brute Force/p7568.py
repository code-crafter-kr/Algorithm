import sys
sys.stdin=open('input.txt','r')

list_A = []
list_B = []
N = int(input())
for i in range (N):
    a = input(). split()
    a = list(map(int,a))
    list_A.append(a) # 몸무게의 집합

for i in range (N):
    a = 0
    for j in range (N):
        if list_A[i][0] < list_A[j][0] and list_A[i][1] < list_A[j][1]:
            a = a + 1
    list_B.append(a)

for i in range (N):
    if i == N-1:
        print(list_B[i]+1)
        break

    print(list_B[i]+1, end = " ")