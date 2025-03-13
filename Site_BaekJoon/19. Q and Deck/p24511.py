from collections import deque
n = int(input())

for i in range(1, 5):
    if i == 1:
        A = list(map(int, input().split()))
    elif i == 2:
        B = list(map(int, input().split()))
    elif i == 3:
        M = int(input())
    elif i == 4:
        C = list(map(int, input().split()))


new_lst = deque()
for i in range(n):
    if A[i] == 0:
        new_lst.append(B[i])
        
if not new_lst:
    for x in C:
        print(x, end = " ")

else:
    for x in C:
        print(new_lst.pop(), end = " ")
        new_lst.appendleft(x)

