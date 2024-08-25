n=int(input())
i=0
flag=False
while True:
    power=pow(2,i)
    if power == n:
        print("YES")
        break
    elif power>n:
        print("NO")
        break
    i+=1