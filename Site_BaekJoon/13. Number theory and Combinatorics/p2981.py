import sys
import numpy as np

sys.stdin = open("input.txt", "r")

case = int(sys.stdin.readline())
lst = np.array([])
lst_A = []
for i in range (case):
    a = int(sys.stdin.readline())
    lst = np.append(lst, np.array([a]))
    lst.sort()

lst_A = [i for i in range (2, int(lst[0])+1)]
for i in lst_A:
    lst_2 = lst % i
    lst_2.sort()
    if lst_2[0] == lst_2[-1]:
        print(i, end = " ")
