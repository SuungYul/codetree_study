from math import ceil
pos = list(map(int, input().split()))

cnt = 0

while True:
    pos.sort()
    if pos[1] - pos[0] == 1 and pos[2] - pos[1] == 1:
        break
    
    if pos[1] - pos[0] < pos[2] - pos[1]:
        if pos[1] - pos[0] == 1:
            pos[0] = min(pos[1] + 2, ceil((pos[1]+pos[2])/2))
            cnt+=1
        else:
            pos[2] = ceil((pos[0]+pos[1])/2)
            cnt+=1
    else:
        if pos[2] - pos[1] == 1:
            pos[2] = max(pos[1] - 2, ceil((pos[0]+pos[1])/2))
            cnt+=1
        else:
            pos[0] = ceil((pos[2]+pos[1])/2)
            cnt+=1    
print(cnt)