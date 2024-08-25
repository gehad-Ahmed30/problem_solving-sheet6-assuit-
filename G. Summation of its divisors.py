import math
n=int(input())
output=[]
flag=0
for i in range(1,int(math.sqrt(n))+ 1):
    if n % i==0:
        output.append(i)
        flag+=1

        if i!=n // i:
            output.append(n // i)
            flag+=1
    

print(sum(output))

