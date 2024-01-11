a, b = map(int, input().split())

list_X = [" " for i in range (a)]
list_T = [i for i in range (1, a+1)]

for i in range (a):
    list_Y = list_X[:]
    if i == 0:
        print("*"*a)
    elif i == a-1:
        print("*"*a)
        break
    else:
        x = 1
        while True:
            if x*b-i > a-1:
                break

            elif x*b-i in list_T:
                list_Y[x*b-i-1] = "*"
                x = x + 1

            else:
                x = x + 1
        list_Y[0], list_Y[-1] = "*", "*"
        for i in range (len(list_Y)):
            if i == len(list_Y)-1:
                print(list_Y[i])
            else:
                print(list_Y[i], end = "")
