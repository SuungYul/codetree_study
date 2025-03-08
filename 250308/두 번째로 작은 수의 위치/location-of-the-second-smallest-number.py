n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
second = -1 if len(set(a))==1 else sorted(set(a))[1]

find = False
ans = -1
for i in range(n):
    if a[i] == second:
        if find:
            ans = -1
        else:
            find = True
            ans = i+1
        

print(ans)
