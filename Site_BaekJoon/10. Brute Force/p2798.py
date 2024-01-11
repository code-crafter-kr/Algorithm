import sys
sys.stdin=open('input.txt','r')

N, M = input(). split()
M, N = int(M), int(N)

list_A = input().split(" ")
list_B = [0]
list_A = list(map(int, list_A))
list_A.sort()
list_A.reverse()
# 3개의 합을 모두 더해주는함수..

for a in range (0, N-2):
    for b in range(1, N-1):
        for c in range(2, N):
            if a != b and a !=c and b !=c:
                d = list_A[a] + list_A[b] + list_A[c]

            if d not in list_B and d <= M and list_B[-1] < d:
                list_B.append(d)

list_B = list(map(int, list_B)) 
list_B.sort()
print(list_B[-1])
