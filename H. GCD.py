x,y=map(int,input().split())
a,b=x,y
while y>0:
     x, y = y, x % y
GCD=x
LCM=int((a*b)//GCD)
print(f"{GCD}  {LCM}")
