n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
arr = [[0]*n for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return x>=0 and x< n and y>=0 and y<n

for point in points:
    arr[point[0]-1][point[1]-1] = 1
    comf_cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = point[0]-1 + dx, point[1]-1 + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            comf_cnt+=1
    
    if comf_cnt == 3:
        print(1)
    else:
        print(0)
