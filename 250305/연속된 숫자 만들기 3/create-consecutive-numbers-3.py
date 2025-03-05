a = list(map(int, input().split()))

# Please write your code here.
cnt = 0

while True:
    a.sort()
    if a[0] + 1 == a[1] and a[1] + 1 ==a[2]:
        break
    
    if a[1] - a[0] > a[2] - a[1]:
        a[2] = a[1] -1
    else:
        a[0] = a[1] + 1
    cnt +=1

print(cnt)