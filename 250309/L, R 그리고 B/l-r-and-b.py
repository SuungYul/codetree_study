board = [list(input()) for _ in range(10)]

# Please write your code here.
l_x = l_y = 0
b_x = b_y = 0
r_x = r_y = 0
for i in range(10):
    for j in range(10):
        if board[i][j] == 'L':
            l_x = j
            l_y = i
        if board[i][j] == 'B':
            b_x = j
            b_y = i
        if board[i][j] == 'R':
            r_x = j
            r_y = i

if (l_x == 0 and b_x == 0 and r_x == 0) or (l_x == 9 and b_x == 9 and r_x == 9):
    print(abs(l_y-b_y)+1)
elif (l_y == 0 and b_y == 0 and r_y == 0) or (l_y == 9 and b_y == 9 and r_y == 9):
    print(abs(l_x-b_x)+1)
else:
    print(abs(l_x-b_x)+abs(l_y-b_y)-1)