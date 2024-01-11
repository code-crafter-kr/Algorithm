# 기본 수학 1 '달팽이는 올라가고 싶다'
A, B, V = input().split()
A = int(A) 
B = int(B) 
V = int(V) 

T = A - B 
V = V - A 

a = V // T 

if V % T == 0:
    print(a+1)
else:
    print(a+2)
