n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!
max_width = 0
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * y2 + x2 * y3 + x3 * y1) - 
               (x2 * y1 + x3 * y2 + x1 * y3))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            if (x[i]==x[j] or x[i]==x[k] or x[j] == x[k]) and (y[i]==y[j] or y[i]==y[k] or y[j]==y[k]):
                 max_width = max(max_width, area(x[i], y[i], x[j], y[j],x[k], y[k]))
        
print(max_width)