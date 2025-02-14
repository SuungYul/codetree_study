T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Write your code here!
cnt = 0
for i in range(a, b+1):
    d1 = d2 = 1000
    for j in range(T):
        if c[j] == 'S':
            d1 = min(d1, abs(i-x[j]))
        else:
            d2 = min(d2, abs(i-x[j]))
    
    if d1 <= d2:
        cnt+=1


print(cnt)
