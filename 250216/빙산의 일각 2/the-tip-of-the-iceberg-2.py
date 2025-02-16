n = int(input())
h = [int(input()) for _ in range(n)]

# Write your code here!

max_cnt = 0

for height in range(1, max(h)):
    result = []
    temp = []
    for i in h:
        if i-height <= 0:
            if temp:
                result.append(temp)
                temp = []
        else:
            temp.append(i-height)

    if temp:  # 마지막 그룹 추가
        result.append(temp)
        
    max_cnt = max(max_cnt, len(result))

print(max_cnt)