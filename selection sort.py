arr = list(map(int,input().split()))

for i in range(len(arr)):
    chk = i
    for j in range(i+1,len(arr)):
        if arr[chk] > arr[j]:
            chk = j
    arr[i], arr[chk] = arr[chk], arr[i]

print(arr)
