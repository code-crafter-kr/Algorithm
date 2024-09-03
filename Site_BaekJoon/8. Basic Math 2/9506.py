def isPerfect(num):
    temp = set()
    temp.add(1)
    for i in range (2, num //2 + 2):
        if num % i == 0:
            temp.add(i)
            temp.add(num // i)
    
    if sum(list(temp)) == num:
        return temp
    else:
        return []

while True:
    n = int(input())
    if n == -1:
        break

    result = sorted(isPerfect(n))

    if len(result) == 0:
        print(str(n) + " is NOT perfect.")
    else:
        print(n, end = " = ")
        for i in range (len(result) - 1):
            print(result[i], end = " + ")
        print(result[-1])
