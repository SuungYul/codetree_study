a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
if a > d or b < c :
    print(b-a + d-c)
else:
    print(max(a,b,c,d) - min(a,b,c,d))