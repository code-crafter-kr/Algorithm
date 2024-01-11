T = int(input())
list_A = []

if T == 1:
    pass

elif T >= 2:
    for i in range (2, T+1):

        while True:
            if T % i == 0:
                list_A.append(i)
                T = T / i
            
            else:
                break

for ii in range (len(list_A)):
    print(list_A[ii])