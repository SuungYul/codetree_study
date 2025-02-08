a, b, c = map(int, input().split())

# Write your code here!

def f(n):
    if n < 10:
        return n
    return n % 10 + f(n//10)

print(f(a*b*c))