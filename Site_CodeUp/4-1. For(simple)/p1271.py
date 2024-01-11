n = int(input())
list_A = input().split()
list_A = list(map(int, list_A))

list_A.sort()
print(list_A[-1])