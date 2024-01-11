# 기본수학 1 문제 '부녀 회장이 될테야!'
T = int(input())

for i in range (T):

    list_B = [i for i in range (1, 15)] # 0층의 original 거주민 수
    list_A = [] # k층까지의 거주민 수의 리스트 자료형
    list_C = [] # 잠시 저장되는 k층의 거주민 수
    list_A.append(list_B)
    k = int(input()) #층수
    n = int(input()) #호수
    A = 0
    while True:
        
        if A == k: #while문 루프 꺠는 제어문
            break
        else:
            A = A + 1

        B = 0 # 거주민 수

        for i in range (0, 14):

            B = B + list_B[i] # 거주민 수 규칙
            list_C.append(B) # C 그릇에 거주민 수를 리스트형으로 추가

        list_B = list_C
        list_A.append(list_C)
        list_C = []

    print(list_A[k][n-1])