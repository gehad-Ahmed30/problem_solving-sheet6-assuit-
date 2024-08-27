import math
x,y=map(int,input().split())
#in python is built in function -> NCR using math.comb()
#in python is built in function -> NPR using math.perm()

result1=math.perm(x,y)
result2=math.comb(x,y)
print(f"{result2} {result1}")
