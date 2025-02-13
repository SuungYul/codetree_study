k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Write your code here!
developers = [set() for _ in range(n+1)]

for i in range(k):
    a = arr[i]
    for j in range(n):
        for k in range(j+1, n):
            developers[a[j]].add(a[k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            continue
        if j in developers[i] and i in developers[j]:
            developers[j].remove(i)
            developers[i].remove(j)

cnt = 0
for d in developers:
    cnt+=len(d)

print(cnt)