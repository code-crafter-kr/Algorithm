n = int(input())
c = n*2 - 1

for i in range (c):
    if i < n:
        print(" " * (n-i-1), end = "")
        print("*" * ((i+1)*2-1))
    else:
        print(" " * (i-n+1), end = "")
        print("*" * ((c-i)*2-1))