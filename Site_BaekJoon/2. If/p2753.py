A = int(input())
if (A%100!=0) & (A%4==0) or (A%400==0):
    print("1")
else:
    print("0")