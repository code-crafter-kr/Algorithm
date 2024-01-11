n = input()

for i in n:
    if i == "x":
        print("a", end = "")
    elif i == "y":
        print("b", end = "")
    elif i == "z":
        print("c", end = "")
    elif i == " ":
        print(" ", end = "")
    else:
        print(chr(ord(i)+3), end = "")