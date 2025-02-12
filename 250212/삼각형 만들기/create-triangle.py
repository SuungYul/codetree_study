n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!
max_width = 0
d = 0
h = 0
for i in range(n):
    for j in range(i+1, n):
        
        if y[i] == y[j]:
            d = max(d, abs(x[i]-x[j]))
        if x[i] == x[j]:
            h = max(h, abs(y[i]-y[j]))

        max_width = max(max_width, d*h)        

print(max_width)