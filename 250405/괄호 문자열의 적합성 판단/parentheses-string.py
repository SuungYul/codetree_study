str = input()

# Please write your code here.
l = []
flag = True
for s in str:
    if s == '(':
        l.append(s)
    else:
        if l:
            l.pop()
        else:
            flag = False

if l:
    flag = False

if flag:
    print('Yes')
else:
    print('No')