n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
i = 0
l = [arr[i]]
while i<n:
    if i < n-1:
        stone = arr[i+1]
        jump = 1
        for j in range(1, k+1):
            if i + j >=n:
                break
            if stone >= arr[i+j]:
                stone = arr[i+j]
                jump = j
        l.append(stone)
        i += jump
    else:
        l.append(arr[i])
        break

print(max(l))