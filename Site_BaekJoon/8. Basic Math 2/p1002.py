import sys
sys.stdin=open('input.txt','r')

T = int(input())

for i in range (T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    A = x1 - x2
    B = y1 - y2 
    D = r1 + r2
    distance = (A ** 2 + B ** 2)**0.5
    if r1 - r2 > 0:
        C = r1 - r2
    else:
        C = r2 - r1


    if x1 == x2 and y1 == y2 and r1 == r2:
        print('-1')

    elif C < distance and D > distance:
        print('2')

    elif D == distance or C == distance:
        print('1')    
    
    elif D < distance or distance < C or distance == 0:
        print('0')
