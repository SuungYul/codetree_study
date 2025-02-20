N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
# Write your code here!

max_len = 0

for i in range(N):
    l = [arr[i]]
    for j in range(i+1, N):
        tmp = list(l) + [arr[j]]
        if max(tmp) - min(tmp) <=K :
            l = tmp
        else:
            break
    max_len = max(max_len, len(l))

print(max_len)
    