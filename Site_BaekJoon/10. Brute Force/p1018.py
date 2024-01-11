import sys
sys.stdin=open('input.txt','r')

V, H = map(int, input().split())

list_input = []
list_A = []

for i in range (V):
    A = input()
    list_input.append(A)

def cal(list_input, M, N):
    a = 0
    for x in range (M, M+8): # 행
        for y in range(N, N+8): # 열
            #첫글자가 B가 기준일때
            if x % 2 == 0 and y % 2 ==0 and list_input[x][y] == "W":
                a = a + 1
            
            elif x % 2 == 0 and y % 2 == 1 and list_input[x][y] == "B":
                a = a + 1
            
            elif x % 2 == 1 and y % 2 == 0 and list_input[x][y] == "B":
                a = a + 1
            
            elif x % 2 == 1 and y % 2 == 1 and list_input[x][y] == "W":
                a = a + 1

    if a > 64 - a:
        return 64 - a
    else:
        return a

for a in range (0, V - 7):
    for b in range (0, H-7):
        list_A.append(cal(list_input, a, b))

list_A.sort()
print(list_A[0])