n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def merge_sort(l, low, high):
    if low  < high:
        mid = (low + high) //2
        merge_sort(l, low, mid)
        merge_sort(l, mid+1, high)
        l = merge(l, low, mid, high)

merged_arr = [0] * n

def merge(l, low, mid, high):
    global merged_arr
    i, j = low, mid+1
    k = low
    while i <= mid and j <= high:
        if l[i] <= l[j]:
            merged_arr[k] = l[i]
            k+=1
            i+=1
        else:
            merged_arr[k] = l[j]
            k+=1
            j+=1
    
    while i <= mid:
        merged_arr[k] = l[i]
        k+=1
        i+=1
    
    while j <= high:
        merged_arr[k] = l[j]
        k+=1
        j+=1
    
    for k in range(low, high+1):
        l[k] = merged_arr[k]

    return l

merge_sort(arr, 0, n-1)
print(*arr)