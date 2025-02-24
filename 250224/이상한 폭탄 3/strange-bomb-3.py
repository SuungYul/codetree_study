N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Write your code here!
d = {idx: 0 for idx in num}

for i in range(N):
    for j in range(i+1, N):
        if num[i] == num[j] and abs(i-j)<=K:
            d[num[i]]+=1

if max(d.values()) == 0:
    print(0)
else:
    print(max(key for key, value in d.items() if value == max(d.values())))