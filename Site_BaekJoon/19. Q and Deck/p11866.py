from collections import deque

a, b = map(int, input().split())
lst = deque()

list_A = []
for i in range(1, a+1):
    lst.append(i)

for ii in range (a):
    for jj in range (b-1):
        a = lst.popleft()
        lst.append(a)
    a = lst.popleft()
    list_A.append(a)

print("<", end = "")
x = list_A.pop()
for j in list_A:
    print(j, end = ", ")
print(x, end = ">")
