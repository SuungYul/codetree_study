N = int(input())
A = []

for _ in range(N):
    line = input().split()
    command = line[0]
    
    if command == 'push_front':
        A.insert(0, int(line[1]))
    elif command == 'push_back':
        A.append(int(line[1]))
    elif command == 'pop_front':
        print(A.pop(0))
    elif command == 'pop_back':
        print(A.pop())
    elif command == 'size':
        print(len(A))
    elif command == 'empty':
        print(0 if A else 1)
    elif command == 'front':
        print(A[0])
    elif command == 'back':
        print(A[len(A)-1])