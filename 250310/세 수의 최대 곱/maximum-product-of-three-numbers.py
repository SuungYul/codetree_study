n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort(reverse=True)
ans = 0
if arr[0] <= 0 or arr[len(arr)-1]>=0:
    ans = arr[0]*arr[1]*arr[2]
else:
    arr.sort(key= lambda x : abs(x), reverse=True)
    ans = arr[0]*arr[1]
    for i in range(2, n):
        if (ans > 0 and arr[i] > 0) or (ans < 0 and arr[i] < 0):
            ans *= arr[i]
            break

print(ans)
            
    
