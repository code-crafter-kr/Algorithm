import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
lst = deque()
for i in range (n):
    command = input().strip()
    try:
        command, value = command.split()
        lst.append(value)
    except:
        if command == "pop":
            try:
                print(lst.popleft())
            except:
                print(-1)
        elif command == "size":
            print(len(lst))
        elif command == "empty":
            if len(lst) == 0:
                print(1)
            else:
                print(0)
        elif command == "front":
            if len(lst) == 0:
                print(-1)
            else:
                print(lst[0])
        elif command == "back":
            if len(lst) == 0:
                print(-1)
            else:
                print(lst[-1])

