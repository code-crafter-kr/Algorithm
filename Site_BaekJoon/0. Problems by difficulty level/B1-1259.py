while True:
    n = input()
    if n == "0":
        break
    
    sw = 0
    for i in range(len(n)):
        if n[i] == n[-1 * (i + 1)]:
            continue
        else:
            print("no")
            sw = 1
            break
    
    if sw == 0:
        print("yes")