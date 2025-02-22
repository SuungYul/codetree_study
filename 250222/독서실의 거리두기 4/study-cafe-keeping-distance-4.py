N = int(input())
seat = list(input())

# Write your code here!
   
def diff(lst):
    m_d = N
    for i in range(N):
        if lst[i] == '1':
            for j in range(i+1, N):
                if lst[j] == '1':
                    m_d = min(m_d, j-i)
    return m_d

max_diff = 0

for i in range(N):
    for j in range(i+1, N):
        if seat[i] == '0' and seat[j] == '0':
            seat[i] = '1'
            seat[j] = '1'
            max_diff = max(max_diff, diff(seat))
            seat[i] = '0'
            seat[j] = '0'

print(max_diff)
            
   