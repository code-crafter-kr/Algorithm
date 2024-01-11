a, b = map(int, input().split())
sum = a * b

lst = list(map(int,input().split()))

for i in lst:
    print(i - sum, end = " ")
