N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

# Please write your code here.
l = [['가위','바위','보'], ['가위', '보', '바위'], ['바위', '가위', '보'], ['바위', '보', '가위'], ['보', '가위', '바위'], ['보', '바위', '가위']]

max_win = 0
for lst in l:
    win = 0
    for i in range(N):
        if lst[a[i]-1] == '가위' and lst[b[i]-1] == '보':
            win +=1
        if lst[a[i]-1] == '바위' and lst[b[i]-1] == '가위':
            win +=1
        if lst[a[i]-1] == '보' and lst[b[i]-1] == '바위':
            win +=1
    max_win = max(max_win, win)

print(max_win)        
        
        