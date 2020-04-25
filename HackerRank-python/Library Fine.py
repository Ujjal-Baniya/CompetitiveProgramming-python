d1,m1,y1 = [int(i) for i in input().split()]
d2,m2,y2 = [int(i) for i in input().split()]
if y1>y2:
    print("10000")
elif y1<y2 or m1<m2:
    print("0")
else:
    if m1>m2:
        print((m1-m2)*500)
    else:
        if d1<=d2:
            print("0")
        else:
            print((d1-d2)*15)
