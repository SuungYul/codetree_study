n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
list_x = [p[0] for p in points]
list_y = [p[1] for p in points]

# Write your code here!
min_cnt = 10**18
for line_x in range(min(list_x)-1, max(list_x)+2, 2):
    for line_y in range(min(list_y)-1, max(list_y)+2, 2):
        dot_list = [0]*4

        for x,y in points:
            if x>line_x and y>line_y:
                dot_list[0]+=1
            if x<line_x and y>line_y:
                dot_list[1]+=1
            if x<line_x and y<line_y:
                dot_list[2]+=1
            if x>line_x and y<line_y:
                dot_list[3]+=1
        
        min_cnt = min(min_cnt, max(dot_list))

print(min_cnt)
            