import sys
sys.stdin = open("input.txt", "r")

case = int(sys.stdin.readline())
lst = []
lst_A = []

for i in range (case):
    lst.append(int(sys.stdin.readline()))
lst.sort()
a = lst[-1]
b = lst[0]

for i in range (2, b + 1):
    if a % i == b % i:
        lst_A.append([i, a % i])

for i in range (1, len(lst)-1):
    a = lst[i]
    for j in lst_A:
        if a % j[0] != j[1]:
            lst_A.remove(j)
