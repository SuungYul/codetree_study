X = int(input())

# Please write your code here.

dist = 0
time = 0
v = 1
while dist < X:
    # print(v)
    time += 1
    dist += v
    if X - dist > sum(range(v+2)):
        v+=1
    elif X - dist >= sum(range(v+1)):
        v = v
    else:
        if v > 1:
            v-=1
    
print(time)