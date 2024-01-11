a ,b = map(int, input().split())
if b < a:
    a, b = b, a 
list_A = []
x = 1
for i in range (1,b+1):
    if i % 2 == 1:
        list_A.append(x)
    else:
        list_A.append(x*10)
        x += 1

print(list_A[a-1]+ list_A[b-1])
