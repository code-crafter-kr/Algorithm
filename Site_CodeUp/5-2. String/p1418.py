N = input()
N = list(N)
for i in range (len(N)):
    if N[i] == "t":
        print(i+1, end = " ")