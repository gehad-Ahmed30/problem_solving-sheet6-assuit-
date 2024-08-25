n = int(input())

low,hight=1,int((2*n)**.5)
while low <= hight:
    mid=(low+hight)//2
    if mid * (mid+1)//2 <=n:
        result=mid
        low=mid+1
    else:
        hight=mid-1

print(result)

#binary search      (log n)