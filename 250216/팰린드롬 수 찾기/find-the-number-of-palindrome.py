X, Y = map(int, input().split())

# Write your code here!

def is_palindrome(n):
    l = list(map(int, str(n)))
    if len(l) % 2 == 1 :
        if l[:len(l)//2] == l[-1:len(l)//2: -1]:
            return True
    else:
        if l[:len(l)//2] == l[-1:len(l)//2-1: -1]:
            return True
    return False

cnt = 0
for i in range(X, Y+1):
    if is_palindrome(i):
        cnt+=1

print(cnt)