import math
x1,y1,x2,y2=map(int,input().split())
a,b=pow((x1-x2),2), (y1-y2)**2
result=math.sqrt(a+b)
print(result)