N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Write your code here!
l = [i for i in range(1, N+1)]

l_a1 = list()
l_b1 = list()
l_c1 = list()

l_a2 = list()
l_b2 = list()
l_c2 = list()


for i in range(-2, 3):
    l_a1.append(l[(a1-i)%N])
    l_b1.append(l[(b1-i)%N])
    l_c1.append(l[(c1-i)%N])

    l_a2.append(l[(a2-i)%N])
    l_b2.append(l[(b2-i)%N])
    l_c2.append(l[(c2-i)%N])

s = set()

for i in l_a1:
    for j in l_b1:
        for k in l_c1:
            s.add((i,j,k))

for i in l_a2:
    for j in l_b2:
        for k in l_c2:
            s.add((i,j,k))

print(len(s))
