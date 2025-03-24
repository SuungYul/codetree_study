n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

while(True):
    sort = True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            sort = False
    
    if sort:
        break

print(*arr)
