N = int(input())
seats = input()

# Please write your code here.
max_d = 0
for i in range(N):
    if seats[i] == '0':
        close_d = N
        for j in range(N):
            if seats[j] == '1':
                close_d = min(close_d, abs(i-j))
        
        max_d = max(max_d, close_d)
    
already_close = N
for i in range(N):
    for j in range(i+1, N):
        if seats[i] == '1' and seats[j] == '1':
            already_close = min(already_close, j-i)


print(min(max_d, already_close))