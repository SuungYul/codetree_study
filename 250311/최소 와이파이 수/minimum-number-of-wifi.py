n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
i = 0  # 직접 인덱스를 제어할 변수

while i < n:
    if arr[i] == 1:
        cnt += 1
        i += 2 * m  # i를 2*m만큼 건너뛰기
    i += 1  # 기본적으로 한 칸씩 이동

print(cnt)
