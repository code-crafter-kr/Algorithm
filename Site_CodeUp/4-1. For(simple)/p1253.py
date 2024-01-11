a, b = map(int, (input().split()))
if b < a:
    a, b = b, a
list_A = [i for i in range (a,b+1)]
list_A.sort()
list_A = list(map(str, list_A))
print(" ".join(list_A))
