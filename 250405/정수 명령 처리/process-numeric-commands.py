N = int(input())
# command = []
value = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        value.append(int(line[1]))
    elif line[0] == "size":
        print(len(value))
    elif line[0] == "empty":
        print(0 if value else 1)
    elif line[0] == "pop":
        print(value.pop())
    else:
        print(value[len(value)-1])

# Please write your code here.
