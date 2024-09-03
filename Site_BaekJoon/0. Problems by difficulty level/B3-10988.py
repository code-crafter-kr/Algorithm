s = input()

start = 0
end = -1

while start <= len(s):
    if start == len(s):
        print(1)
        break
    elif s[start] == s[end]:
        pass
    else:
        print(0)
        break
    
    start += 1
    end -= 1