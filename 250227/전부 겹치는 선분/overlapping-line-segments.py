n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.
l = {idx: 0 for idx in range(min(x1), max(x2)+1)}

for x, y in segments:
    for i in range(x, y+1):
        l[i]+=1

print('Yes' if n in l.values() else 'No')
