C = int(input())
for i in range(C):
    B = 0
    D = 0
    E = 0

    A_list = input(). split()
    A_list = list(map(int, A_list))
    
    for i in range (A_list[0]):
        B = B + A_list[i+1]
        E = B / A_list[0] # E = 평균

    for i in range (A_list[0]):

        if (A_list[i+1]) > E :
            D = D + 1  # D = 평균을 넘는 학생의 수
    

    F = (D / A_list[0] * 100)
    
    X = "{0:0.3f}".format(F)
    print("%s%%" %X)