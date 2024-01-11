arr = input()
arr = list(arr)

N = len(arr)
for ii in range(N):
    for jj in range(N-ii-1):
        if arr[jj]>arr[jj+1]:
            arr[jj],arr[jj+1] = arr[jj+1],arr[jj]
arr.reverse()

for i in range (len(arr)):
    if i == len(arr)-1:
        print(arr[i])
        break
    print(arr[i], end="")
