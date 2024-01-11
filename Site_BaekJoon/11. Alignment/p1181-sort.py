import sys
sys.stdin=open('input.txt','r')

N = int(sys.stdin.readline())
list_A = [sys.stdin.readline().rstrip() for i in range (N)]


for i in range (len(list_A)):
    list_A[i] = [len(list_A[i]), list_A[i]]

list_A.sort()

a = 0
for i in list_A:
    if i[1] != a:
        print(i[1])

    a = i[1]