n = int(input())
arr = list(input().split())
sorted_arr = sorted(arr)
# Please write your code here.
cnt = 0

i = 0
while i < n-1:
    if arr == sorted_arr:
        break
    if ord(arr[i]) > ord(arr[i+1]):
        tmp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = tmp
        cnt+=1
        if i > 0:
            i-=1
    else:
        i+=1
print(cnt)