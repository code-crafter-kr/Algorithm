def ret(n, list_X):
    if n == 1:
        return list_X

    else:
        for xx in range (n-(int(n/3)*2), l, n): #27 > 
            for ii in range (xx, xx+int(n/3)):
                list_X[ii] = list(list_X[ii])
                for yy in range (n-(int(n/3)*2), l, n):
                    for jj in range (yy, yy + int(n/3)):
                        list_X[ii][jj] =" "
                list_X[ii] = "".join(list_X[ii])

        return ret(int(n/3), list_X)

def make(n):
    list_A = []
    for i in range (n):
        list_A.append("*"*n)
    return list_A

l = int(input())
list_p = make(l) # 리스트 만들어주기
list_p = ret(l, list_p)

for ii in list_p:
    print(ii)