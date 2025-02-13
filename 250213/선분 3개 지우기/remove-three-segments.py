n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
# Write your code here!

def f(l):
    l.sort()
    for i in range(len(l)):
        a, b = l[i]
        for j in range(i+1, len(l)):
            c,d = l[j]
            if b >= c :
                return False
    
    return True

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = list(arr)
            del tmp[k]
            del tmp[j]
            del tmp[i]
            # print(tmp, f(tmp))
            if f(tmp):
                cnt+=1

print(cnt)

