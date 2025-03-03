a, b, x, y = map(int, input().split())

# Please write your code here.
print(min(abs(b-a), abs(a-x)+abs(b-y), abs(a-y)+abs(b-x)))

