N = int(input())
str = input()

# Write your code here!

cnt = 0
for i in range(N):
    s = str[:i+1]
    if s in str[i+1:]:
        cnt = len(s)
    else:
        break

print(cnt+1)