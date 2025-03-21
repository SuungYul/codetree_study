n, m = map(int, input().split())


arr = list(map(str, input()))
p = n
for _ in range(m):
    n = len(arr)
    cmd = input().split()
    command = cmd[0]
    if command == 'L':
        if p != 0:
            p-=1
    elif command == 'R':
        if p != n:
            p+=1
    elif command == 'D':
        if p!= n:
            arr.pop(p)
    elif command == 'P':
        if p == n:
            arr.append(cmd[1])
        else:
            arr.insert(p, cmd[1])
        p+=1
print(''.join(arr))
