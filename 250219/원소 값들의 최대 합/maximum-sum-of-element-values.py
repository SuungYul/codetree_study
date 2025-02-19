n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))

# Write your code here!
max_sum = 0
for i in range(1, n+1): # 시작위치
    res = 0
    arr = list(a)
    start = arr[i]
    for j in range(m):
        temp = arr[start]
        arr[start] = start
        res += start
        start = temp
        
    max_sum = max(max_sum, res)

print(max_sum)