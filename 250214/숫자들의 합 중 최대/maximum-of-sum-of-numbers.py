X, Y = map(int, input().split())

# Write your code here!
m = 0
for i in range(X, Y+1):
    l = list(map(int, str(i)))
    m = max(m, sum(l))

print(m)