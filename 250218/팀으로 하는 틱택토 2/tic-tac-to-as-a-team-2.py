inp = [list(map(int,input())) for _ in range(3)]

# Write your code here!
cnt = 0
already = list()
for i in range(3):
    s = set(inp[i])
    if len(s) == 2:
        tmp = sorted(s)
        if tmp not in already:
            cnt+=1
            already.append(tmp)
        


for i in range(3):
    s = set([inp[0][i], inp[1][i], inp[2][i]])
    if len(s) == 2:
        tmp = sorted(s)
        if tmp not in already:
            cnt+=1
        already.append(tmp)

s = set([inp[0][0], inp[1][1], inp[2][2]])
if len(s) == 2:
    tmp = sorted(s)
    if tmp not in already:
        cnt+=1
    already.append(tmp)
s = set([inp[2][0], inp[1][1], inp[0][2]])
if len(s) == 2:
    tmp = sorted(s)
    if tmp not in already:
        cnt+=1
    already.append(tmp)

print(cnt)