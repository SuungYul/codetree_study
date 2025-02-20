N = int(input())
seat = input()

# Write your code here!

no_empty_list = []
for i, s in enumerate(seat):
   if s == '1':
       no_empty_list.append(i)


def find_near(idx):
    min_diff = 10**9
    res = -1
    for e in no_empty_list:
        if min_diff > abs(e - idx):
            min_diff = abs(e - idx)
            res = e
    
    return res

max_d = 0

for i in range(N):
    if seat[i] == '0':
        max_d = max(max_d, abs(i - find_near(i)))

print(max_d)