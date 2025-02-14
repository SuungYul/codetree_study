N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
A = [t[0] for t in ranges]
B = [t[1] for t in ranges]
# Write your code here!
m = 0
for i in range(min(A)-1, max(B)+2):
    s = 0
    for a, b in ranges:
        if i < a:
            s+=C
        elif a<=i and i<=b:
            s+=G
        else:
            s+=H
    m = max(m, s)

print(m)

