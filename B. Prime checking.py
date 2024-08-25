import math
n=int(input())

if n==1:
    print("NO")
else:
    flag=True
    for i in range(2,int(math.sqrt(n)) + 1):      #limit memory
      if n%i==0:
        flag=False
        break
    if flag:
      print("YES")
    else:
      print("NO")

