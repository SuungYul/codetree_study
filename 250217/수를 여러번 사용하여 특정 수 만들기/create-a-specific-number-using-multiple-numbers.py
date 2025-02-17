A, B, C = map(int, input().split())

# Write your code here!

max_result = 0

for i in range(C // A + 1):
    for j in range(C // B + 1):
        if A * i + B * j <= C:
            max_result = max(max_result, A * i + B * j)

print(max_result)
