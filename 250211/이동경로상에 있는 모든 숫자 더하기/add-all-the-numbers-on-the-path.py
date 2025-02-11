N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Write your code here!
def in_range(x, y):
    return x>=0 and x<N and y>=0 and y<N

x, y = (N-1)//2, (N-1)//2

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
dn = 0

result = board[x][y]

nx, ny = x + dxs[dn], y + dys[dn]

for s in str:
    if s == 'F':
        if in_range(nx, ny):
            x, y = nx, ny
            result += board[x][y]
    elif s == 'R':
        dn = (dn+1)%4
    else:
        dn = (dn-1 +4)%4


    nx, ny = x + dxs[dn], y + dys[dn]

print(result)