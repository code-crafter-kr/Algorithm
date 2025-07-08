import sys
from collections import deque

input = sys.stdin.readline 


n = int(input())

lst = deque()
for _ in range(n):
    command = input()

    if command[0] == "f":
        print(lst[0] if lst else -1)

    elif command[0] == "b":
        print(lst[-1] if lst else -1)

    elif command[0] == "s":
        print(len(lst))

    elif command[0] == "e":
        print(1 if not lst else 0)

    elif command[0:2] == "po":
        print(lst.popleft() if lst else -1)

    else:
        lst.append(int(command.split()[-1]))
