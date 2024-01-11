x , y = input().split()
list_A = [chr(i) for i in range (ord(x), ord(y)+1)]
list_A.sort()
list_A = list(map(str, list_A))
print(" ".join(list_A))