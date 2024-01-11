import sys
sys.stdin=open('input.txt','r')

N = int(input())
T = input(). split(" ")
b = 0

for i in range (N):
    a = int(T[i])
    if a == 1:
        b = b + 1

    for ii in range (2, a):
        if a % ii == 0:
            b = b + 1
            break

print(N-b)