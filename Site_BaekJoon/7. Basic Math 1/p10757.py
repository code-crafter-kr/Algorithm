# 기본 수학 1 '큰수 A+B'
A,B = input().split()
list_A = []
list_B = []
C = 0
for i in range (len(A)):
    list_A.append(A[i])

for i in range (len(B)):
    list_B.append(B[i])

list_A.reverse()
list_B.reverse()

for i in range (len(A)):
    C = C + int(list_A[i])*(10**i)
for i in range (len(B)):
    C = C + int(list_B[i])*(10**i)

print(C)