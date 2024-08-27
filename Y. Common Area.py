def cal_common_area(output):
     x1, y1, x2, y2=output[0]
     for i in output[1:]:
        x1 = max(x1, i[0])
        y1 = max(y1, i[1])
        x2 = min(x2, i[2])
        y2 = min(y2, i[3])

        if x1 >= x2 or y1 >= y2:
            return 0
        
     return (x2 - x1) * (y2 - y1)


n=int(input())
for i in range(1,n+1):
    N=int(input())
    output=[]
    for j in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        output.append((x1, y1, x2, y2))

    result=cal_common_area(output)
    print(f"Case #{i}: {result}")