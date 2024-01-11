
import sys
sys.stdin = open("input.txt" , "r")

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split())) # time O(N)

X = int(sys.stdin.readline())
lst2 = list(map(int,sys.stdin.readline().split()))

for i in lst2:
    if i in lst:
        print(1,end =" ")
    else:   
        print(0, end = " ")