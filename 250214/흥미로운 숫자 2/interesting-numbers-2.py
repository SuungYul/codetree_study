X, Y = map(int, input().split())

# Write your code here!
cnt = 0

for i in range(X, Y+1):
    l = list(map(int, str(i)))
    s = set(map(int, str(i)))
    if len(s) == 2:    
        d = dict()
        for j in s:
            d[j] = 0
        
        for j in l:
            d[j]+=1
        
        a, b = d.values()
        
        if (a>1 and b == 1) or (a == 1 and b>1):
            cnt+=1
        
    


print(cnt)