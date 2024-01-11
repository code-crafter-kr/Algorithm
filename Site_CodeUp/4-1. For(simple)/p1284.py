for n in range (1000000, 1001000):
    list_A = []
    list_C = []
    if n == 1:
        print("wrong number")

    for i in range (1,n+1):
        if n % i == 0:
            list_A.append(i)

    for i in list_A:
        list_B = []
        for ii in range(1, i+1):
            if i % ii == 0:
                list_B.append(ii)
        if len(list_B) == 2:
            list_C.append(i)
    if len(list_C) > 4:
        print(n, list_C)