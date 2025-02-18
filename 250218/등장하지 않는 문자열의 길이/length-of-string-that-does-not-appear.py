N = int(input())
str = input()

# Write your code here!

cnt = 0
for i in range(N):
    for j in range(i+1, N):   
        s = str[i:j]
        if s in str[j:]:
            cnt = max(cnt,len(s))
        else:
            break

print(cnt+1)