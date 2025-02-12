n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
min_width = 10**9

for i in range(n):
    l = points[:i] + points[i+1:]
    x = [p[0] for p in l]
    y = [p[1] for p in l]

    width = (max(x)-min(x))*(max(y)-min(y))
    if width>0:
        min_width = min(min_width, width)

print(min_width)
