n = int(input())
list_A = [" " for i in range (n)]
for i in range (n):
    if i == 0:
        print("*" * n)
    elif i == n-1:
        print("*" * n)
    else:
        list_B = list_A[:]

        list_B[0] = "*"
        list_B[-1] = "*"
        list_B[i] = "*"
        list_B[n-i-1] = "*"
        for i in range (len(list_B)):
            if i != (len(list_B)-1):
                print(list_B[i], end="")
            else:
                print(list_B[i])