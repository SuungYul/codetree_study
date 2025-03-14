n = int(input())
arr = list(map(int, input().split()))
# arr.sort()
reverse_arr = sorted(arr, reverse=True)
# Please write your code here.
l = []
for i in range(n):
    l.append((reverse_arr[i], reverse_arr[i+n]))
    # print(l)

l.sort(key= lambda x : abs(x[0]-x[1]) )
print(l[0][0]-l[0][1])