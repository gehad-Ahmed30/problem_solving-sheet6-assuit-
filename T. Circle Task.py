def check(x,y,r,point):
    for a,b in point:
        cal_dist=(a-x)**2 +(b-y)**2
        if cal_dist<=r**2:
           print("YES")
        
        else:
           print("NO")

x,y,r,p=map(int,input().split())
point=[]
for i in range(p):
    a,b=map(int,input().split())
    point.append((a,b))

check(x,y,r,point)