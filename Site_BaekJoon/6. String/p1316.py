import sys
sys.stdin=open('input.txt','r')

N = int(input())
A = 0
for i in range (N):
    L = input()
    Error = 0
    for i in range (len(L)-1):
        if L[i] != L[i+1]:
            B = L[i]
            F = L[i+2:]
        
            for ii in range (len(F)):
                if F[ii] == B:
                    Error = Error+1
    if Error > 0:
        A = A + 1
        
print(N-A)


