from collections import deque
n = int(input())
cmd = []
num = deque()

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "push_front":
        num.appendleft(int(line[1]))
    elif line[0] == "push_back":
        num.append(int(line[1]))
    elif line[0] == "pop_front":
        print(num.popleft())
    elif line[0] == "pop_back":
        print(num.pop())
    elif line[0] == "size":
        print(len(num))
    elif line[0] == "empty":
        print(1 if not num else 0)
    elif line[0] == "front":
        print(num[0])
    elif line[0] == "back":
        print(num[len(num)-1])
