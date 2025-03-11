n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
p = sum(blocks)//n
ans = 0
for b in blocks:
    ans+=abs(p-b)

print(ans//2)