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
            d = max(d, abs(x[i]-x[j]))
        for k in range(n):
            if k == i or k == j:
                continue
            if x[i] == x[j]:
                h = max(h, abs(y[i]-y[j]))

            max_width = max(max_width, d*h)        

print(max_width)