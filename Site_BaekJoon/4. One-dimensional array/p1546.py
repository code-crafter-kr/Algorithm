N = int(input())

A_list = input(). split()

B = int()
C = 0

A_list = list(map(int , A_list))
A_list.sort()
B = A_list[-1]
for i in range(N):
    C = C + A_list[i]

print(C/B*100/N)
