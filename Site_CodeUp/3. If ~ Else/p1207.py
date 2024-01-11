a, b, c, d = input().split()

list = [a,b,c,d]

if list.count("1") == 0:
    print("모")
elif list.count("1") == 1:
    print("도")
elif list.count("1") == 2:
    print("개")
elif list.count("1") == 3:
    print("걸")
else:
    print("윷")
 