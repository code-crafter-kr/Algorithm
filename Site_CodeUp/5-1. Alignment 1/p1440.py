n = int(input())

list_A = list(map(int, input().split()))

for ii in range (n):
    print(ii+1, end=": ")
    for jj in range (n):
        if ii == jj:
            pass
        else:
            if list_A[ii] > list_A[jj]:
                print(">", end = " ")
            elif list_A[ii] < list_A[jj]:
                print("<", end = " ")
            else:
                print("=", end = " ")
    print("\n", end ="")