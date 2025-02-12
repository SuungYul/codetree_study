n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!
min_d = 10**18

for i in range(n):
    for j in range(i+1,n):
        d = (x[i]-x[j])**2 + (y[i]-y[j])**2
        min_d = min(min_d, d)

print(min_d)