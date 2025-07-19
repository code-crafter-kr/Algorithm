import sys
input = sys.stdin.readline

n = int(input())

lst = dict()

for i in range(1, 21):
    lst[i] = False

for i in range(n):
    command = input()

    if command[0] == "r":
        lst[int(command[7:])] = False
    
    elif command[0] == "c":
        print(int(lst[int(command[6:])]))

    elif command[0] == "t":
        num = int(command[7:])
        if lst[num] == True:
            lst[num] = False
        else:
            lst[num] = True
    
    elif command[0] == "e":
        for i in range (1, 21):
            lst[i] = False
    
    elif command[0:2] == "al":
        for i in range (1, 21):
            lst[i] = True
    
    else:
        lst[int(command[4:])] = True
