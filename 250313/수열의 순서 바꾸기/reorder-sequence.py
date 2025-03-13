n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

for cnt in range(n-1, 1, -1):
    if sequence[cnt] < sequence[cnt-1]:
        break

print(0 if sequence == sorted(sequence) else cnt)