n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def f(result,idx):
    if idx == n-1:
        return result
    return f((result * arr[idx+1])//gcd(min(result, arr[idx+1]), max(result, arr[idx+1])), idx+1)

print(f(arr[0],0))
