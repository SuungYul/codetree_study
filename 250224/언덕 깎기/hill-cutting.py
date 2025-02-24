def min_cost_bruteforce(heights):
    ans = float('inf')

    for start in range(0, 84):  # 언덕 높이 범위가 최대 100이므로, 구간 [start, start+17]의 최대값이 100을 넘지 않게 설정
        end = start + 17
        cost = 0

        for h in heights:
            if h < start:
                cost += (start - h) ** 2
            elif h > end:
                cost += (h - end) ** 2

        ans = min(ans, cost)

    return ans

# 입력 처리
n = int(input())
heights = [int(input()) for _ in range(n)]

# 결과 출력
print(min_cost_bruteforce(heights))
