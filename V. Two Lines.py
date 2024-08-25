x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
a,b=x2-x1,y2-y1
c,d=x4-x3,y4-y3
if a*d ==b*c:
    print("YES")
else:
    print("NO")