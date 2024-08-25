a,b,z=map(int,input().split())
x=z % 3
if x==1:
    print(a)
elif x==2:
    print(b)
else:
    print(a^b)