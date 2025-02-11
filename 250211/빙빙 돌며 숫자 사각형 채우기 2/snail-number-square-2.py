n, m = map(int, input().split())

# Write your code here!
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

dn = 0

arr = [[0]* m for _ in range(n)]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

x, y = 0, 0
arr[x][y] = 1

nx, ny = x + dxs[dn], y + dys[dn]

for i in range(2, n*m +1):
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dn = (dn+1)%4
    x, y = x + dxs[dn], y + dys[dn]
    arr[x][y] = i
    nx, ny = x + dxs[dn], y + dys[dn]

for a in arr:
    print(*a)
