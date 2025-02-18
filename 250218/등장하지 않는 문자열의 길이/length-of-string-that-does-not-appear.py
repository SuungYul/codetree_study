n = int(input())
s = input()

ans = 0

for i in range(1, n):  # 길이 i의 부분 문자열 검사
    seen = set()  # 중복 확인을 위해 `set` 사용
    success = True  

    for j in range(n - i + 1):  # 모든 부분 문자열 검사
        tmp = s[j:j+i]
        
        if tmp in seen:  # 중복 존재하면 실패
            success = False
            break
        
        seen.add(tmp)  # 새로운 부분 문자열 저장

    if success:  # 중복이 없는 첫 번째 길이 찾으면 종료
        ans = i
        break

print(ans)
