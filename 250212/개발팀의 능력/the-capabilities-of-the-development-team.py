arr = list(map(int, input().split()))

# Write your code here!
min_diff = 10**9

for i in range(5):
    for j in range(i+1, 5):
        sum1 = arr[i] + arr[j]

        for k in range(5):
            for l in range(k+1, 5):
                if i == k or i == l or j == k or j == l:
                    continue
                sum2 = arr[k] + arr[l]

                sum3 = sum(arr) - sum1 - sum2
                
                if sum1 != sum2 and sum1!=sum3 and sum2!=sum3:
                    min_diff = min(min_diff, max(sum1, sum2, sum3)-min(sum1, sum2, sum3))

print(min_diff if min_diff!=10**9 else -1)
