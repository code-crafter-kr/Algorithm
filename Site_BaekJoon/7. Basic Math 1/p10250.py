# 기본수학 1 문제 'ACM 호텔'
import sys
sys.stdin=open('input.txt','r')

T = int(input())
for i in range (T):    
    H, W, N = input().split()
    H = int(H) # 층 수
    N = int(N) # 몇번째 손님
    A = N // H #호수
    B = N % H #층수

    if A < 9 and (B != 0):
        A = A + 1
        A = str(A)
        A = "0" + A 
        B = str(B)    
        print(B + A)
    elif A >= 9 and (B != 0):
        A = A + 1
        A = str(A)
        B = str(B)    
        print(B + A)

    if B == 0:
        H = str(H)
        if A <= 9:
            A = str(A)
            A = "0" + A 
            print(H + A)
            
        elif A > 9:
            A = str(A)  
            print(H + A)
