list_A = [i for i in range (1,int(input())+1)]

for i in range (len(list_A)-1):
    list_A.remove(int(input()))

print(list_A[0])