from collections import deque

n, k = map(int, input().split())

# Please write your code here.

q = deque()

for i in range(1, n+1):
    q.append(i)

while len(q)!= 0:
    for _ in range(k-1):
        q.append(q.popleft())
    print(q.popleft(), end = ' ')