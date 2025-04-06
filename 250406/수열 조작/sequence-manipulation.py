from collections import deque
n = int(input())

# Please write your code here.
q = deque()
q.extend(i for i in range(1, n+1))

while len(q)>1:
    q.popleft()
    q.rotate(-1)

print(q.pop())