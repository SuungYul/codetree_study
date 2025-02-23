n = int(input())
adjacent = list(map(int, input().split()))

# Write your code here!

l = list()

for i in range(1,n+1):
    l.clear()
    l.append(i)
    for j in range(n-1):
        if abs(adjacent[j] - l[len(l)-1]) in l:
            continue
        l.append(abs(adjacent[j] - l[len(l)-1]))
    
    if len(l) == n:
        break

print(*l)