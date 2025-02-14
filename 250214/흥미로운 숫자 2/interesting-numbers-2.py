X, Y = map(int, input().split())

# Write your code here!
cnt = 0

for i in range(X, Y+1):
    l = list(map(int, str(i)))
    s = set()
    for j in l:
        s.add(j)
    if len(s) == 2:
        cnt+=1

print(cnt)