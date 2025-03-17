n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]


# Please write your code here.
min_v = 1000
for i in range(n):
    tmp = segments[:i] + segments[i+1:]
    x1 = [a[0] for a in tmp]
    x2 = [a[1] for a in tmp]
    min_v = min(min_v, max(x2)-min(x1))

print(min_v)