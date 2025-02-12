ability = list(map(int, input().split()))

# Write your code here!
min_diff = 100000000

def get_diff(i, j):
    sum1 = ability[i] + ability[j]
    md = 100000000
    for k in range(5):
        for m in range(k+1,6):
            if i!=k and i!=m and j!=k and j!=m:
                if md > abs(ability[k] + ability[m] - sum1):
                    md = abs(ability[k] + ability[m] - sum1)
                    sum2 = ability[k] + ability[m]

    
    sum3 = sum(ability) - sum1 - sum2

    return max(sum1, sum2, sum3) - min(sum1, sum2, sum3)


for i in range(5):
    for j in range(i+1, 6):
        min_diff = min(min_diff, get_diff(i, j))

print(min_diff)