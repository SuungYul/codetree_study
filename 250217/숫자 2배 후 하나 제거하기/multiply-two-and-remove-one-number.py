n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

def diff_neighbor(l):
    diff_sum = 0
    for i in range(len(l)-1):
        diff_sum+=abs(l[i]-l[i+1])

    return diff_sum

result = 10**18

for i in range(n):
    temp = list(arr)
    temp[i] = temp[i]*2
    for j in range(n):
        temp2 = list(temp)
        del temp2[j]
        result = min(result, diff_neighbor(temp2))

print(result)