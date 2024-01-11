from collections import deque
import sys

sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())


for i in range (T):
    q = 0
    z = 0
    deck = deque()
    order = sys.stdin.readline().rstrip()

    n = int(sys.stdin.readline())

    arr = sys.stdin.readline().split(",")
    arr[0] = arr[0][1:]
    arr[-1] = arr[-1][:-2]

    if arr == ['']:
        arr = []

    for jj in arr:
        deck.append(jj)

    #덱생성기

    for ii in range (len(order)):
        if "R" == order[ii:ii+1]:
            q += 1
        else:
            if q % 2 == 0:
                try:
                    deck.popleft()
                except:
                    z = 1
                    break
            else:
                try:
                    deck.pop()
                except:
                    z = 1
                    break

    if q % 2 == 1:
        deck.reverse()


    if z == 1:
        print("error")

    else:
        if len(deck) == 0:
            print("[]")
        else:
            print("[", end ="")
            for x in range (len(deck)):
                if x == (len(deck)-1):
                    print(deck[x], end ="]\n")
                else:
                    print(deck[x], end= ",")