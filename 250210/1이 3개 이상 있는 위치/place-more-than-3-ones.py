n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return x >= 0 and x<=n-1 and y>=0 and y<=n-1

cnt = 0

for i in range(n):
    for j in range(n):
        near_cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                near_cnt+=1
        if near_cnt >=3:
            cnt+=1
            

print(cnt)