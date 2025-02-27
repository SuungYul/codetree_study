a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.
if a < d or b > c :
    print(max(a,b,c,d) - min(a,b,c,d))
else:
    print(b-a + d-c)