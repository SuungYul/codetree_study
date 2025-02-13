n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Write your code here!
l = [0] * max(b)
max_time = 0

for i in range(n):
    t = times[:i]+times[i+1:]
    l = [0] * max(b)
    for i, j in t:
        for k in range(i, j):
            l[k] = 1
    max_time = max(max_time, sum(l))

print(max_time)