n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Please write your code here.
un_read = [chr(i) for i in range(ord('A'), ord('A')+n)]
print(un_read)
for i in range(p-1, m):
    if u[i] == 0:
        un_read.clear()
    if c[i] in un_read:
        un_read.remove(c[i])

print(*un_read)

