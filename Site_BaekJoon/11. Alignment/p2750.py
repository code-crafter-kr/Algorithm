# buble sort
N = int(input())
arr = [int(input()) for _ in range (N)]

N = len(arr)
for ii in range(N):
    for jj in range(N-ii-1):
        if arr[jj]>arr[jj+1]:
            arr[jj],arr[jj+1] = arr[jj+1],arr[jj]
for i in arr:
    print(i)

# selection sort
N = int(input())
arr = [int(input()) for _ in range (N)]

N = len(arr)
for ii in range (N):
    min_pos = ii
    for jj in range (ii+1, N):
        if arr[jj] < arr[min_pos]:
            min_pos = jj
    arr[ii], arr[min_pos] = arr[min_pos], arr[ii]

for i in arr:
    print(i)

# insertion sort
N = int(input())
arr = [int(input()) for _ in range (N)]

N = len(arr)
for ii in range (1, N):
    for jj in range (ii, 0, -1):
        if arr[jj] >= arr[jj-1]: #1 , 0
            break
        else:
            arr[jj], arr[jj-1] = arr[jj-1], arr[jj]

for i in arr:
    print(i)