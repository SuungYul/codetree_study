abilities = list(map(int, input().split()))

# Write your code here!

def get_min(i, j, k):
    sum1 = abilities[i] + abilities[j] + abilities[k]
    sum2 = sum(abilities) - sum1
    return abs(sum1-sum2)
min_sum = 1000000
for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            min_sum = min(min_sum, get_min(i, j, k))

print(min_sum)