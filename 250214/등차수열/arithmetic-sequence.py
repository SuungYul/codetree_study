n = int(input())
a = list(map(int, input().split()))

# Write your code here!

def f(l): # l은 정렬된 상태로 오자
    if len(l) == 1:
        return False
    diff = l[1] - l[0]
    for i in range(1, len(l)-1):
        if l[i+1] - l[i] != diff:
            return False
    
    return True
max_c = [0] * 100
for K in range(2, 100):
    a.append(K)
    max_cnt = 0
    for size in range(2, len(a)):
        split_lst = [a[i:i+size] for i in range(0, len(a), size)]
        cnt = 0
        for l in split_lst:
            l.sort()
            if f(l):
                cnt+=1
        max_cnt = max(max_cnt, cnt)
    max_c[K-1] = max_cnt
    a.remove(K)

print(max(max_c))
