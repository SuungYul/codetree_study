n = int(input())
ch, s = [], []
for _ in range(n):
    ci, si = input().split()
    ch.append(ci)
    s.append(int(si))

# Please write your code here.
best = ['A', 'B', 'C']
a = b = c = 0

def find_best(A,B,C):
    global best
    tmp = []
    if A==B and B==C:
        tmp.append('A')
        tmp.append('B')
        tmp.append('C')
    elif A==B and A>C:
        tmp.append('A')
        tmp.append('B')
    elif A>B and A>C:
        tmp.append('A')
    elif B==C and B>A:
        tmp.append('B')
        tmp.append('C')
    elif B>C and B>A:
        tmp.append('B')
    elif C==A and C>B:
        tmp.append('A')
        tmp.append('C')
    elif C>A and C>B:
        tmp.append('C')
    
    if best == tmp:
        return False
    else:
        best = tmp
        return True
cnt = 0
for i in range(n):
    if ch[i] == 'A':
        a+=s[i]
    elif ch[i] == 'B':
        b+=s[i]
    else:
        c+=s[i]
    
    if find_best(a,b,c):
       cnt+=1

print(cnt) 