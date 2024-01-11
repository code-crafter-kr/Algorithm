import sys
sys.stdin=open('input.txt','r')

N = int(sys.stdin.readline())

def re(x):
    list_A = []
    for i in range (x):
        a = int(sys.stdin.readline())
        if a != 0:
            list_A.append(a)
        else:
            list_A.pop()

    return sum(list_A)

print(re(N))