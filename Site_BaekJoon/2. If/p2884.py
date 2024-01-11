A, B = input(). split()
A = int(A)
B = int(B)
if B>=45:
    print(A,B-45)
elif A!=0 and B<45:
    print(A-1, 60+B-45)
else:
    print("23", 60+B-45)