n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
cost = 0

for i in range(n):
    cost += (A[i] - B[i])*(n-i-1)

print(cost)