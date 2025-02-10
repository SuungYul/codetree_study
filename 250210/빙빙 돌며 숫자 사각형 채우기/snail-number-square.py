n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Write your code here!
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<m

x, y = 0, 0
dir_num = 0
arr[x][y] = 1
for i in range(2, n*m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny]!=0:
        dir_num = (dir_num+1)%4
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i
   

for a in arr:
    print(*a)