commands = input()

# Write your code here!
cnt = 0

x, y = 0, 0
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dir_num = 0

for c in commands:
    if c == "L":
        dir_num = (dir_num - 1 + 4) % 4
    elif c == "R":
        dir_num = (dir_num + 1)% 4
    else:
        x, y = x + dxs[dir_num], y + dys[dir_num]
    
    cnt += 1

    if x== 0 and y == 0:
        
        print(cnt)
        break

if x!= 0 or y != 0:
    print(-1)