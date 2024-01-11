A = int(input())
B = int(input())
C = int(input())

D = A * B * C

D  = str(D)

for i in range(10):
    i = str(i)
    print(D.count(i))
