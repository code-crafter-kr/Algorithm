n = input()

for i in n:
    if i == "a":
        print("x", end = "")
    elif i == "b":
        print("y", end = "")
    elif i == "c":
        print("z", end = "")
    elif i == " ":
        print(" ", end = "")
    else:
        print(chr(ord(i)-3), end = "")