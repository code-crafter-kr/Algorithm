import sys
sys.stdin=open('input.txt','r')

N = int(sys.stdin.readline())
list_A = []
for i in range (N):
    X = sys.stdin.readline().rstrip()
    if X[:4] == "push":
        list_A.append(int(X[5:]))

    elif X[:3] == "top":
        if list_A == []:
            print(-1)
        else:
            print(list_A[-1])
            
    elif X[:4] == "size":
        print(len(list_A))

    elif X[:5] == "empty":
        if list_A == []:
            print("1")
        else:
            print("0")

    else:        
        if list_A == []:
            print("-1")
        else:
            print(list_A.pop())