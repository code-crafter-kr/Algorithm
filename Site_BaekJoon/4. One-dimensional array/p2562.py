A_list = []
A_list = list(map( int , A_list))

for i in range(9):
    B = int(input())
    A_list.append(B)
B_list = A_list[:]

A_list.sort()
C = A_list[-1]
print(C)

D = int(B_list.index(C))

print(D+1)