n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Write your code here!
max_score = 0
for i in range(1, 4):
    my_cup = i
    score = 0
    for j in range(n):
        if a[j] == my_cup:
            my_cup = b[j]
        elif b[j] == my_cup:
            my_cup = a[j]
        
        if my_cup == c[j]:
            score+=1
    
    max_score = max(max_score, score)

print(max_score)