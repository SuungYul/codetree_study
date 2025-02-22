nums = list(map(int, input().split()))

# Write your code here!
nums.sort()
A = nums[0]
B = nums[1]
if A + B == nums[2]:
    C = nums[3]
    l = list(nums[4:])
else:
    C = nums[2]
    l = list(nums[3:])

for i in l:
    if A+B == i or A+C == i or B+C == i or A+B+C == i:
        l.remove(i)

D = l[0]

print(A,B,C,D)
    

