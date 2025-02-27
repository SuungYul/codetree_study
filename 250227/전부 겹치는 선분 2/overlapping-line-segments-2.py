n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.
possible = False
for i in range(n):
    tmp = segments[:i] + segments[i+1:]
    
    x = [t[0] for t in tmp]
    y = [t[1] for t in tmp]
    
    if min(y) <= max(x):
        possible = True

print("Yes" if possible else "No")