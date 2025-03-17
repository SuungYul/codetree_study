arr = list(map(int, input().split()))
arr.sort()
# Please write your code here.
a = arr[0]
b = arr[1]
c = arr[2]
d = arr[len(arr)-1] - (a+b+c)
print(a,b,c,d)