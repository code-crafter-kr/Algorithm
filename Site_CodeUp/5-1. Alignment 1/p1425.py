import sys
sys.stdin = open("input.txt", "r")
a, b = input().split()
a, b = map(int, (a, b))

list_A = input().split()
list_A = list(map(int, list_A))
list_A.sort()
x = 0
while True:
    if list_A == []:
        break

    if len(list_A) > b:
        for i in range (b):
            print(list_A.pop(0), end = " ")

    else:
        for i in range (len(list_A)):
            print(list_A.pop(0),end = " ")
    print("\n", end ="")
    

