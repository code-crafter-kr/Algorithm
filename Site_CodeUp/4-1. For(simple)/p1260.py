a,b = map(int,(input().split()))
list_A = [i for i in range (a, b+1)]
x = 0
for i in list_A:
    if i%3 == 0:
        x += i
print(x)