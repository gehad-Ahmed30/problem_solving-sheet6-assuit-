x,y,z=map(int,input().split())
max_num=max(x,y)
min_num=min(x,y)
result=1
for i in range(min_num,max_num+1):
    result*=i
    result%=z
print(result)
