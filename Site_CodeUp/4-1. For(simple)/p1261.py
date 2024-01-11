import random

list_A = input().split()
list_A = list(map(int, list_A))

list_B = []
for i in list_A:
    if i % 5 == 0:
        list_B.append(i)

if list_B == []:
    print(0)
else:
    print(random.choice(list_B))