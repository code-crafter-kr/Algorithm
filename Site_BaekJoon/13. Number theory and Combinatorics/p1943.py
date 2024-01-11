import sys
sys.stdin = open("input.txt" , "r")

case = int(sys.stdin.readline())
for i in range (case):
    a, b = map(int, sys.stdin.readline().split())
    if b > a:
        a , b = b, a
    for i in range (b, 0, -1):
        if a % i == 0 and b % i == 0:
            x = i
            break
    
    print(int(a * b / i))