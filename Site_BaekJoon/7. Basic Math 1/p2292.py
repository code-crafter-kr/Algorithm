#수학 문제 1 '벌집'

N = int(input())
a = 1
b = 0
if N == 1:
    print("1")

else:
    while N > a:
        b = b + 1
        a = a + 6*b
        
    print(b+1)