n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Write your code here!
s = set()
for i in range(a[0], b[0]+1):
    s.add(i)

for i in range(1,n):
    for s1 in list(s):
        x = s1 * (2**(i+1))
        if x < a[i] or x > b[i]:
            s.remove(s1)

print(min(s))
        