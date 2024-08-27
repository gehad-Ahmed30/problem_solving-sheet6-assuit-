n=int(input())
j=0
for i in range(n):   #line
    flag=1
    for j in range(i+1):   #number in line
        print(int(flag) ,end=' ')
        flag=flag*(i-j)/(j+1)
    
    print()
    flag=1

