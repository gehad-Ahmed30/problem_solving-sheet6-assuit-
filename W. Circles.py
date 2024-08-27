import math
def check(x1,y1,x2,y2,x3,y3,x4,y4):
    c1_x=(x1+x2)/2
    c1_y=(y1+y2)/2

    c2_x=(x3+x4)/2
    c2_y=(y3+y4)/2

    dist_c1=(math.sqrt((x1-x2)**2 + (y1-y2)**2))/2   
    dist_c2=math.sqrt(((x3-x4)**2 + (y3-y4)**2))/2

    line=math.sqrt((c1_x-c2_x)**2 +(c1_y-c2_y)**2)
    test_line=dist_c1+dist_c2

    if line>test_line:
        print("NO")
    else:
        print("YES")


x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
check(x1,y1,x2,y2,x3,y3,x4,y4)