n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))  # 1-based index 적용

max_sum = 0

for i in range(1, n+1):  # 시작 위치
    res = 0
    visited = set()  # 방문한 위치 저장
    start = i  # 시작값 설정

    for j in range(m):
        if start in visited:  # 이미 방문한 곳이면 탈출 (사이클 감지)
            break
        visited.add(start)

        res += start  # 현재 위치 값 누적
        start = a[start]  # 다음 이동 위치

    max_sum = max(max_sum, res)  # 최대값 갱신

print(max_sum)
