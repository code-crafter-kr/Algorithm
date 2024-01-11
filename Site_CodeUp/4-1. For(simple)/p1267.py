n = int(input())
list_A = input().split()
list_A = list(map(int, list_A))
a = 0
for i in list_A:
    if i % 5 == 0:
        a = a + i
print(a)