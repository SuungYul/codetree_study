n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Write your code here!
dxs = [1, 0, 0, -1]
dys = [0, 1, -1, 0]
if d == 'U':
    direction = 3
elif d=='D':
    direction = 0
elif d=='R':
    direction = 1
else:
    direction = 2

def movable(x, y):
    return x>=1 and x<=n and y>=1 and y<=n

while t>=1:
    if movable(r+dxs[direction], c+dys[direction]):
        r, c = r+dxs[direction], c+dys[direction]
    else:
        direction = (direction + 3)%4
    t-=1

print(r, c)