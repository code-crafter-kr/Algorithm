import sys
sys.stdin=open('input.txt','r')

N = int(input())
input = sys.stdin.readline
list_A = [input().rstrip() for i in range (N)]

for i in list_A:
    while True:
        if list_A.count(i) > 1:
            list_A.remove(i)
        
        if list_A.count(i) == 1:
            break

N = len(list_A)

for ii in range(N): #순서대로 줄 세우기
    for jj in range(N-ii-1):
        if len(list_A[jj]) > len(list_A[jj+1]):
            list_A[jj], list_A[jj+1] = list_A[jj+1], list_A[jj]

for ii in range (N): #알파벳 순서에 따라 줄 세우기
    for jj in range (N - ii - 1):
        if len(list_A[jj]) == len(list_A[jj+1]):
            a = 0 
            while True:
                if list_A[jj][a] == list_A[jj+1][a]:
                    a = a + 1
                elif list_A[jj][a] > list_A[jj+1][a]:
                    list_A[jj], list_A[jj+1] = list_A[jj+1], list_A[jj]
                    break
                else:
                    break

for i in list_A:
    print(i)