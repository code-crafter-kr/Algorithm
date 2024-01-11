import sys
sys.stdin=open('input.txt','r')

list_A = []
def deter(a):
    for n in range(2, int(a**0.5)+1):
            if a % n == 0 :
                return False
    return True

for i in range(2, 10001):
    if deter(i):
        list_A.append(i) # 1부터 10000까지의 소수 모임


T = int(input())
for ii in range (T):
    N = int(sys.stdin.readline())
    list_B = []
            
    for i in list_A:
        if i > N:
            break
        if N - i in list_A and N-i >= i:
            list_B.append(i)

    print(list_B[-1], N-list_B[-1])