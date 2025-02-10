N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Write your code here!
x, y = 0, 0
cnt = 0
f = False
for i in range(N):
    for _ in range(dist[i]):
        if dir[i] == "N":
            y+=1
        elif dir[i] == "S":
            y-=1
        elif dir[i] == "E":
            x+=1
        elif dir[i] == "W":
            x-=1
        cnt+=1

        if x ==0 and y == 0:
            f = True
            break
    if f:
        break

print(-1 if not f else cnt)

        
        