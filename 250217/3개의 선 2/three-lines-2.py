n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# x, y = zip(*points)
# x, y = list(x), list(y)

# Write your code here!

for i in range(11):
    for j in range(i+1, 11):
        for k in range(j+1, 11):
            tmp = [False] * n
            for idx, (x, y) in enumerate(points):
                if x == i or y == i:
                    tmp[idx] = True
                if x == j or y == j:
                    tmp[idx] = True
                if x == k or y == k:
                    tmp[idx] = True
               
                
                
            if False not in tmp:
                print(1)
                exit()
            

print(0)
            
                
                
        
