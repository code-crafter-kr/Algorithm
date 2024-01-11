n = input()
a = 0
for i in range (0, len(n)+1):
    if n[i] in ["+", "-", "*", "/"]:
        a = int(n[0:i])
        n = n[i:]
        break


while True:
    if n[0] == "=":
        break

    if n[0] == "+":
        for i in range (1, len(n)):
            if n[i] in ["+", "-", "*", "/", "="]:
                b = int(n[1:i]) 
                n = n[i:]
                a = a + b
                break

    elif n[0] == "-":
        for i in range (1, len(n)):
            if n[i] in ["+", "-", "*", "/", "="]:
                b = int(n[1:i]) 
                n = n[i:]
                a = a - b
                break
    elif n[0] == "*":
        for i in range (1, len(n)):

            if n[i] in ["+", "-", "*", "/", "="]:
                b = int(n[1:i]) 
                n = n[i:]
                a = a * b
                break

    elif n[0] == "/":
        for i in range (1, len(n)):
            if n[i] in ["+", "-", "*", "/", "="]:
                b = int(n[1:i]) 
                n = n[i:]
                a = int(a / b)
                break


print(a)


