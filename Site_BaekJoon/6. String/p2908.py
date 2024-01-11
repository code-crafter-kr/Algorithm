A, B = input(). split()

New_A = int(A[0])+ (int(A[1])*10) + (100 * int(A[2]))
New_B = int(B[0])+ (int(B[1])*10) + (100 * int(B[2]))
if New_A > New_B:
    print(New_A)
else:
    print(New_B)