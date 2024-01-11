list = input().split()

if list[2] == "L":
    for i in range (int(list[0])):
        print(" "*i, end ="")
        print("*"*(int(list[1])))

else:
    for i in range (int(list[0])-1,-1, -1):
        print(" "*i, end = "")
        print("*"*(int(list[1])))
