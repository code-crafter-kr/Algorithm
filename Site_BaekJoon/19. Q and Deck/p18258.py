from collections import deque
import sys

N = int(sys.stdin.readline())
deck = deque()

for i in range (N):
    order = sys.stdin.readline()
    if order[:4] == "push":
        deck.append(int(order[5:]))

    elif order[:5] == "front":

        try:
            print(deck[0])
        except:
            print(-1)

    elif order[:4] == "back":

        try:
            print(deck[-1])
        except:
            print(-1)

    elif order[:4] == "size":
        print(len(deck))
    
    elif order[:5] == "empty":
        if len(deck) != 0:
            print(0)
        else:
            print(1)
    
    else:
        try:
            print(deck.popleft())
        
        except:
            print(-1)