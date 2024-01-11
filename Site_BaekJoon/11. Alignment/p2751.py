import sys
sys.stdin=open('input.txt','r')

N = int(sys.stdin.readline())
list_A = [int(sys.stdin.readline()) for i in range (N)]

list_A.sort()

for ii in list_A:
    print(ii)