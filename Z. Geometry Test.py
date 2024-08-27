import math
x,y=map(int,input().split())

if x*2 <= y:
    print("Square")
elif x*2 > math.sqrt((y**2)+(y**2)):
    print("Circle")
else:
    print("Complex")