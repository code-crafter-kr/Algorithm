import sys
sys.stdin=open('input.txt','r')

A = int(input())

for i in range (A):
    B , C = input() . split()
    B = int(B)

    for f in C:
        print (f * B, end="")
    
    print("")

