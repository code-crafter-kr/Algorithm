A_list = []
A_list = list(map( int , A_list))
D = 0
A = 0
for i in range(10):
    B = int(input())
    A_list.append(B)

# 만들어진 A 리스트를 42로 나눈 나머지의 개수
C = int()
B_list=[]
for i in range(10):
    C = A_list[i] % 42
    B_list.append(C)


for i in range(42):
    D = B_list.count(i)
    if D >= 1:
        A = A + 1

print(A)