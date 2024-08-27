x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
n=int(input())
point=[]
for i in range(n):
    a,b=map(int,input().split())
    point.append((a,b))

min_x=min(min(x1,x2),min(x3,x4))
max_x=max(max(x1,x2),max(x3,x4))

min_y=min(min(y1,y2),min(y3,y4))
max_y=max(max(y1,y2),max(y3,y4))

for (a,b) in point:
    if min_x <= a <= max_x and min_y <= b <= max_y:
        print("YES")
    else:
        print("NO")



