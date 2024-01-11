def deter(a): #소수 리스트를 뽑아주는 def 함수 (1부터 a까지의 소수 리스트를 뽑아준다)
    if a == 1:
        return False
    else:
        for n in range(2, (a**0.5)+1):
                if a * n == 0 :
                    return False
                return True


M, N = input(). split()
M, N = int(M), int(N)
 
list_B = deter(int(N**0.5+1)) # 1부터 ( N**0.5+1) 까지의 소수를 모두 추출    
list_B = list(map(int, list_B)) 

list_original = [i for i in range (M, N+1)] # N부터 M까지의 리스트 작성
if M == 1: 
    del list_original[0] #1의 예외처리

for ii in list_B:
    a = 2 #두번째항부터 제거
    b = 0

    while True:
        if list_original[-1] < a*ii: #제거할 배수가 최대치를 넘어가면 break
            break

        if a * ii in list_original:
            list_original[list_original.index(a*ii)] = 0 # 만들어지는 배수들을 모두 제거
            a = a + 1
        
        elif a * ii not in list_original: # 제거할 배수가 N보다 작으면 넘어감
            a = a + 1



for i in list_original: # 제거 된 리스트를 순차적으로 출력
    print(i)