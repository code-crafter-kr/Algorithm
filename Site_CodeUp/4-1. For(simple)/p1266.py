n = int(input())
list_A = input().split()
list_A = list(map(int, list_A))
a = 0
for i in list_A:
    a = a + i
print(a)