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

for ii in range (N):
    min_pos = ii #첫번째 항이 min_position이 된다.
    for jj in range (ii + 1, N): # 두번째항부터 끝항까지 비교
        if len(list_A[min_pos]) > len(list_A[jj]): #두번째 항과 비교 min_pos의 길이와 두번째 항과 비교 두번째항이 더 짧다면 min_pos = 그 항으로 전환
            min_pos = jj
    list_A[ii], list_A[min_pos] = list_A[min_pos], list_A[ii]



#같은 글자 수 일때 우선순위 결정 selection 방법으로.
for ii in range(N): 
    min_pos = ii
    for jj in range (ii+1, N):
        a = 0 #알파벳이 몇번째 있는지 제어 해주는 함수
        if len(list_A[min_pos]) == len(list_A[jj]):
            while True:
                if ord(list_A[min_pos][a]) == ord(list_A[jj][a]):
                    a = a + 1
                elif ord(list_A[min_pos][a]) < ord(list_A[jj][a]):
                    break
                else:
                    min_pos = jj
                    break
    list_A[ii], list_A[min_pos] = list_A[min_pos], list_A[ii]

for i in list_A:
    print(i)            

