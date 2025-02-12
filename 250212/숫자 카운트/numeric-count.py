n = int(input())
conditions = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            valid = True
            for number, cnt1, cnt2 in conditions:
                x, y, z = map(int, str(number))
                exact = (x == i) + (y == j) + (z == k)
                misplaced = ((x == j) or (x == k)) + ((y == i) or (y == k)) + ((z == i) or (z == j))
                if exact != cnt1 or misplaced != cnt2:
                    valid = False
                    break
            if valid:
                count += 1

print(count)
