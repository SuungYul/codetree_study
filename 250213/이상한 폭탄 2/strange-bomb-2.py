N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Write your code here!

bomb = set()

# 이중 루프 돌아서 인덱스 차이가 k이내면 bomb에 추가 max(bomb)가 정답인듯
for i in range(N):
    for j in range(i+1, N):
        if j - i <= K and num[j] == num[i]:
            bomb.add(num[i])


print(max(bomb) if bomb else -1)