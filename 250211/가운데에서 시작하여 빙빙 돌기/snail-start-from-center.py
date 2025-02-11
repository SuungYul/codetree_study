n = int(input())
grid = [[0] * n for _ in range(n)]

# Write your code here!
dxs = [0, -1, 0, 1]
dys = [-1, 0, 1, 0]

dn = 0

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

x, y = n-1, n-1

arr = [[0]*n for _ in range(n)]

arr[x][y] = n*n

nx, ny = x + dxs[dn], y + dys[dn]

for i in range(n*n-1, 0, -1):
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dn = (dn+1)%4
    x, y = x + dxs[dn], y + dys[dn]
    arr[x][y]=i
    nx, ny = x + dxs[dn], y + dys[dn]

for a in arr:
    print(*a)