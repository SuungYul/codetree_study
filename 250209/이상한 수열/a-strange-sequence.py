N = int(input())

# Write your code here!

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f(int(n/3)) + f(n-1)

print(f(N))