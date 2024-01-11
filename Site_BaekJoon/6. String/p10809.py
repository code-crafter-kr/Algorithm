L = input()
F = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in F:
    if i != 'z':
        D = L.find(i)
        print(D, end = " ")
    else:
        D = L.find('z')
        print(D)
