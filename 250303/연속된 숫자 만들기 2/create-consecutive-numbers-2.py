pos = list(map(int, input().split()))
pos.sort()
# Please write your code here.
# pos[0] pos[1] pos[2]
if pos[1]-pos[0] == 1 and pos[2] - pos[1] == 1:
    print(0)
elif pos[1]-pos[0] == 1 or pos[2]-pos[1] == 1 or pos[1]-pos[0] == 2 or pos[2] - pos[1] == 2:
    print(1)
else:
    print(2)