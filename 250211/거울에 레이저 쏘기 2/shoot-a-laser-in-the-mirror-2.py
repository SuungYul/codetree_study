n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Write your code here!
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

q = k // n
r = k % n
if r == 0:
    q -=1
    r += n
x, y = 0,0
if q == 0:
    y = r-1
elif q == 1:
    y = n-1
    x = r-1
elif q == 2:
    x = n-1
    y = (n - r)
else:
    x = (n - r)

cnt = 1

# q가 0일땐 \ 를 만나면 3이되어야하고, /를 만나면 1이 되어야하고
# q가 1일땐 \ 를 만나면 2이 되어야하고, /를 만나면 0이 되어야하고
# q가 2일땐 \ 를 만나면 1이 되어야하고, /를 만나면 3이 되어야하고
# q가 3일땐 \ 를 만나면 0이 되어야하고, /를 만나면 2이 되어야하고

def find_dir(dn, ch):
    if ch == "\\":
        if dn == 0 or dn == 2:
            dn = (dn -1 + 4)%4
        else:
            dn = (dn+1+4)%4
    else:
        if dn == 1 or dn == 3:
            dn = (dn -1 + 4)%4
        else:
            dn = (dn+1+4)%4
    
    return dn
q = find_dir(q, grid[x][y])

nx, ny = x + dxs[q], y + dys[q]

def in_range(x1, y1):
    return x1>=0 and x1<n and y1>=0 and y1<n

while in_range(nx, ny):
    cnt+=1
    x, y = nx, ny
    q = find_dir(q, grid[x][y])
    nx, ny = x + dxs[q], y + dys[q]
    

print(cnt)

