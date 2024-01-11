import sys
sys.stdin=open('input.txt','r')

N = int(input())
list_A = [sys.stdin.readline().rstrip() for i in range (N)]

# 중복되는 단어 제거
for i in list_A:
    while True:
        if list_A.count(i) > 1:
            list_A.remove(i)

        if list_A.count(i) == 1:
            break
#글자 수에 따라 순서대로 줄세우기 selection 방법으로.
N = len(list_A)
for ii in range (1, N):
    for jj in range (ii, 0, -1): # 1부터 시작
        if len(list_A[jj]) >= len(list_A[jj-1]):
            break
        else:
            list_A[jj], list_A[jj-1] = list_A[jj-1], list_A[jj]

for ii in range(1, N): 
    for jj in range (ii, 0, -1):
        a = 0 #알파벳이 몇번째 있는지 제어 해주는 함수
        if len(list_A[jj]) == len(list_A[jj-1]):
            while True:
                if ord(list_A[jj][a]) == ord(list_A[jj-1][a]):
                    a = a + 1
                elif ord(list_A[jj][a]) > ord(list_A[jj-1][a]):
                    break
                else:
                    list_A[jj], list_A[jj-1] = list_A[jj-1],list_A[jj]
                    break

for i in list_A:
    print(i)