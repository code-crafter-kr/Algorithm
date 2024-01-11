list_A = [i for i in range (1,7)]

n = int(input())
for i in list_A:
    for j in list_A:
        if i + j == n:
            print(i, j)