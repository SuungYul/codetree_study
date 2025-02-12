n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!
max_width = 0
d = 0
h = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if y[i] == y[j]:
            d = abs(x[i]-x[j])
        for k in range(n):
            if x[k] == x[i]:
                h = abs(y[k]-y[i])
            if x[k] == x[j]:
                h = abs(y[k]-y[j])
            max_width = max(max_width, d*h)        

print(max_width)