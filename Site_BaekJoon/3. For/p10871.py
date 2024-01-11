N, X = input(). split()
N = int(N)
X = int(X)

A_list = input() . split()

for i in range(N):
    A_list[i] = int(A_list[i])
    if A_list[i] < X:
        print(A_list[i], end=" ")