N, L = map(int, input().split())
a = list(map(int, input().split()))

# 기존 get_score: 추가 점수 없이 기본 h‑score 계산
def get_score(lst: list):
    lst.sort()
    max_score = 0
    for i in range(len(lst)):
        if i >= 1 and lst[i] == lst[i - 1]:
            continue
        if len(lst) - i >= lst[i]:
            max_score = max(max_score, lst[i])
    return max_score

base_h = get_score(a)
# print("기본 h‑score:", base_h)  # 참고용

# extra point를 분배했을 때 최대 h‑score를 구하는 방법
# h‑score 후보 h를 달성하려면, 상위 h개의 논문이 h점 이상이 되어야 합니다.
# extra point로 보충해야 하는 총 점수 합이 L 이하면 h를 달성할 수 있습니다.

# 내림차순 정렬: 상위 h개의 논문을 쉽게 고르기 위해
a_desc = sorted(a, reverse=True)

def can_achieve(h):
    total_extra = 0
    # 상위 h개의 논문에 대해 h 점 이상이 되도록 필요한 추가 점수를 계산
    for i in range(h):
        if a_desc[i] < h:
            total_extra += (h - a_desc[i])
    return total_extra <= L

# 이분 탐색으로 최대 h‑score 후보 결정 (범위: 0 ~ N)
low, high = 0, N
best = base_h  # 최소한 기본 h‑score는 달성할 수 있음

while low <= high:
    mid = (low + high) // 2
    if can_achieve(mid):
        best = mid  # mid값을 달성할 수 있으면 기록 후 더 큰 값 탐색
        low = mid + 1
    else:
        high = mid - 1

print(best)
