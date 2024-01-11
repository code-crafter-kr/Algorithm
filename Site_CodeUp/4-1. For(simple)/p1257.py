a, b = map(int,input().split())
list_A = [i for i in range(a, b+1)]
list_B = [i for i in list_A if i % 2 == 1]
list_B = list(map(str, list_B))
print(" ".join(list_B))