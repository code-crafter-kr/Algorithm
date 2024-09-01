import sys
sys.stdin = open("input.txt", "r")
n = int(input())

lst = [1]
for i in range (1, 44):
    lst.append(lst[i-1] + (i+1))

def check(num):
    for x in lst:
        for y in lst:
            for z in lst:
                if x + y + z == num:
                    return True

length = len(lst)
for i in range (n):
    num = int(input())
    if check(num):
        print(1)
    else:
        print(0)