N = int(input())
numbers = list(map(int, input().split()))
odd = []
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
# Please write your code here.
# 짝수와 홀수를 따로 저장한다

next = 0
cnt = 0

while True:
    if not odd and (not even or (even and next % 2 == 1)):
        break
    if next % 2 == 0:
        if even:
            even.pop()
        else:
            if len(odd)>=2:
                odd.pop()
                odd.pop()
            else:
                break
        cnt+=1
        next+=1
    else: # 홀수
        odd.pop()
        if not even and len(odd) == 4:
            odd.pop()
            odd.pop()
        cnt+=1
        next+=1

print(cnt)
        
    