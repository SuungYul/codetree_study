n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
a = b = 0
situation = 1 # 1 : 동점, 2 : A가 1위, 3 : B가 1위
cnt = 0
for i in range(n):
    if c[i] == 'A':
        a += s[i]
    else:
        b += s[i]
    if a > b:
        if situation != 2:
            situation = 2
            cnt+=1
    elif a < b:
        if situation != 3:
            situation = 3
            cnt+=1
    else:
        if situation != 1:
            situation = 1
            cnt+=1

print(cnt)
                