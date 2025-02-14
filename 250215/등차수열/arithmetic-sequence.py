n = int(input())
a = list(map(int, input().split()))

# Write your code here!
max_cnt = 0
for K in range(1, 101):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) / 2 == K:
                cnt+=1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
