# 함수 문제 '셀프 넘버'

list_A = [i for i in range (10000)]
list_N = []
for B in range (1, 2):

    while B < 10000:
        A = 0
        B = str(B)
        list_N = []

        for i in B:
            A = A + int(i)

        B = A + int(B)
        
        if B < 10000:
            list_N.append(B)