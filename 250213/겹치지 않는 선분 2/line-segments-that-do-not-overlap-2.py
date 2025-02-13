n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
cnt = 0
for i, (x1, x2) in enumerate(lines):
    isPossible = True
    for j, (x3, x4) in enumerate(lines):
        if i == j:
            continue
        if x3 > x1 and x4 < x2:
            isPossible = False
        if x3 < x1 and x4 > x2:
            isPossible = False
    
    if isPossible:
        cnt+=1

print(cnt)
        