N, L = map(int, input().split())
a = list(map(int, input().split()))
def max_h_score(n, l, arr):
    answer = 0
    
    for i in range(1, 101):  # H-Score 후보 (1~100)
        cnt = 0
        cnt_check = 0
        
        for j in range(n):
            if arr[j] >= i:
                cnt += 1
            elif arr[j] + 1 >= i:
                if cnt_check < l:
                    cnt += 1
                    cnt_check += 1
        
        if cnt >= i:
            answer = i
    
    return answer

print(max_h_score(N, L, a))  # 최대 H-Score 출력

