arr = list(map(int, input().split()))
arr.sort()
# Please write your code here.
a, b = arr[0], arr[1]
if a+b != arr[2]:
    c = arr[2]
else:
    c = arr[len(arr)-1]-(a+b)

print(a,b,c)