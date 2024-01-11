n = int(input())
a = 0
for i in range (n+1, 0, -1):
    print(" "*a, end = "")
    print("*"*(i-1))
    a = a+1
    if a == n:
        break