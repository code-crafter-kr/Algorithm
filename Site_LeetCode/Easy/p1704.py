def halvesAreAlike(s):
    lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s1, s2 = 0, 0

    for i in range (0, len(s)//2):
        if s[i] in lst:
            s1 += 1
    for j in range (i+1, len(s)):
        print(s[j])
        if s[j] in lst:
            s2 += 1
    return s1 == s2
    

print(halvesAreAlike("book"))