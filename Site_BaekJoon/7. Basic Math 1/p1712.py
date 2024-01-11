# 기본 수학1 '손익 분기점'

A, B, C =input() . split()
A = int(A)
B = int(B)
C = int(C)

i = 0

if 0 <= B - C:
    print("-1")

else:
    i = A / (C - B)
    i = int(i)
    print(i+1)