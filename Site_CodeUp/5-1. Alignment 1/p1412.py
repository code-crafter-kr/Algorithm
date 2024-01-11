n = input()
n = list(n)
list_X = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_D = [0 for _ in range (26)]
for ii in n:
    for jj in range (26):
        if ii == list_X[jj]:
            list_D[jj] = list_D[jj] + 1
            break

for i in range (26):
    print(list_X[i],end =":")
    print(list_D[i])
