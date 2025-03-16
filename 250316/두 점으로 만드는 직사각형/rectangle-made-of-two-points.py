x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.
print(max(abs(x1-a2), abs(x2-a1))*max(abs(y1-b2), abs(y2-b1)))