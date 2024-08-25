x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
a=(y3-y2)*(x2-x1)
b=(x3-x2)*(y2-y1)
if a==b:
    print("YES")
else:
    print("NO")