import math
x,y,z=map(int,input().split())
if x+y>z and x+z>y and y+z>x:
    s = (x + y + z) / 2  
    area = math.sqrt(s * (s - x) * (s - y) * (s - z))
    print("Valid")
    print(area)
else:
    print("Invalid")