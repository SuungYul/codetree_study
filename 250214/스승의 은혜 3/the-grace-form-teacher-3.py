N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
gifts.sort(key=lambda x: (x[0]+x[1]))
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Write your code here!
max_cnt = 0

for i in range(N):
    if P[i] // 2 + S[i] > B:
        continue
    # sum_p = P[i] // 2 + S[i]
    bound = B - P[i] // 2 - S[i]
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        if P[j] + S[j] > bound:
            continue
        bound = bound - (P[j] + S[j])
        # sum_p += P[j] + S[j]
        cnt+=1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)