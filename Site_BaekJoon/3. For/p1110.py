N  = int(input())
if N < 10:
    N = N * 10

X = N
X=int(X)
T=int()
A = 0
while True:
    T = (X // 10) + (X % 10)
    X = 10 * (X%10) + T%10
    A = A+1
    if (N==X):
        break

print(A)