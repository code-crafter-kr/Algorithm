n = int(input())
N = (n // 2) + 1
X = (n // 2)
for i in range (N):
    print(" "*(X), end= "")
    print("*"*(2*i+1))
    X = X - 1