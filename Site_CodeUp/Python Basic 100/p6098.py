Y = [list(map(int,input().split())) for _ in range(10)]
# for i in range (0,10):  
#     X = input() #1 1 1 1 1 1 1 1 1 1 / 1 0 0 1 0 0 0 0 0 1
#     X = X.split(" ")
#     X = list(map(int, X))
#     Y.append(X)

a = 1
b = 1

while True:
    if Y[a][b] == 2: #먹이를 만나면 스탑
        Y[a][b] = 9
        break
    
    elif a == 8 and b == 8: #맨 오른쪽 끝 아래로 왔을때 스탑
        Y[a][b] = 9
        break

    elif Y[a][b+1] == 1 and Y[a+1][b] == 1: #갈 자리가 없을때 스탑
        Y[a][b] = 9
        break

    elif Y[a][b+1] != 1: 
        Y[a][b] = 9 #오른쪽 자리가 0일때 다음자리가 9
        b = b + 1

    elif Y[a][b+1] == 1:
        Y[a][b] = 9
        a = a + 1
      
for i in Y:
    i = list(map(str, i))
    print(" ".join(i))
