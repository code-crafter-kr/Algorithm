from collections import deque
import sys

sys.stdin = open("input.txt", "r")
n = int(input())

for i in range (n):
    list_A = deque()
    y = 0
    a, b= map(int, input().split())
    list_Z = list(map(int, input().split()))
    list_Z[b] += 0.1 #수에 특별성을 부여 (중복되는 중요도)
    x = list_Z[b]

    for ii in range (len(list_Z)):
        list_A.append(list_Z[ii]) #받은 list_Z = deque화

    while len(list_A) > 0:

        if max(list_A) - 0.1 > list_A[0]:
            list_A.rotate(-1)

        else:
            z = list_A.popleft()
            y += 1
            if z == x:
                print(y)
                break
