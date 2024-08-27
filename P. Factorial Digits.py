import math
n=int(input())
flag=1
for i in range(1,n+1):
    flag*=i

num_digit=math.floor(math.log10(flag)+1)

print(f"Number of digits of {n}! is {num_digit}")

