n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
max_cnt = 0
for a1, b1 in pairs:
    cnt = 0
    for a2, b2 in pairs:
        if (a1 == a2 and b1 == b2) or (a1==b2 and b1 == a2):
            cnt+=1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)