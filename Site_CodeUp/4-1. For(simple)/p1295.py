n = input()
list_l = [chr(i) for i in range(97, 123)]
list_u = [chr(i) for i in range(65, 91)]
for i in n:
    if i in list_l:
        print(i.upper(), end = "")
    elif i in list_u:
        print(i.lower(), end = "")
    else:
        print(i, end = "")