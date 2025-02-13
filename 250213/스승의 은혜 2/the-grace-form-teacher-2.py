N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Write your code here!
max_p = [0]* B

P.sort(reverse=True)

for i in range(N):
    sum_p = P[i] // 2
    cnt = 1
    bound = B - sum_p
    for j in range(i+1, N):
        if P[j] > bound:
            break
        bound -= P[j]
        cnt+=1
        sum_p+=P[j]
    
    max_p[B-bound-1] = max(max_p[B-bound-1],cnt)

print(max(max_p))