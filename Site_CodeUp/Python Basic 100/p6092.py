a = int(input())
b = input().split()
list_A = [i for i in range (1,24)]
list_A = list(map(str, list_A))

for i in list_A:
    print(b.count(i), end= " ")