N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.
cnt = 0
p = [-1] * 11
for i in range(N):
    if p[pigeon[i]] != -1 :
        if p[pigeon[i]] != position[i]:
            cnt+=1
            p[pigeon[i]] = position[i]
    else:
        p[pigeon[i]] = position[i]

print(cnt)