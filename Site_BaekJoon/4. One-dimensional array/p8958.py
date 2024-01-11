N = int(input())
for f in range (N):
    A = str(input())
    D = 0
    B = 0
    C = 0
    for i in range (len(A)):
        if (len(A) - 1 == i) & (A[len(A)-1] == "O"): 
            B = B + 1
            C = B*(B+1)/2
            D = D + C

        elif (len(A) - 1 == i) & (A[len(A)-1] == "X"):
            C = B*(B+1)/2
            D = D + C
    
        elif A[i] == "X":
            C = B*(B+1)/2
            D = D + C
            B = 0
            C = 0

        elif A[i] == "O":
            B = B + 1

    D = int(D)
    print(D)