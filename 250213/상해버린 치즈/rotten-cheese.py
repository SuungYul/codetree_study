N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Write your code here!

c_p = list()
possible_sick_cheese = [False] * M
for _ in range(M):
    c_p.append(set()) 

for i in range(D):
    person = p[i]
    cheese = m[i]
    time = t[i]
    c_p[cheese-1].add(person)
    for j in range(S):
        sick_person = sick_p[j]
        sick_time = sick_t[j]
        
        for c in range(M):
            if sick_person in c_p[c]:
                if time + 1  <=sick_time:
                    possible_sick_cheese[c] = True
                else:
                    possible_sick_cheese[c] = False
max_p = 0
for c in range(M):
    if possible_sick_cheese[c]:
        max_p = max(max_p, len(c_p[c]))

print(max_p)
            



