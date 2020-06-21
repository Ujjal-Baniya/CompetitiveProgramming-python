#greatest gcd
l = [int(x) for x in input().split()]
cnt = 0
for i in range(len(l)):
    if i==0:
        if len(l)==1:
            print(1)
            break
        else:
            if l[i]<l[i+1]:
                cnt+=1
    elif i == len(l)-1:
        if l[i]>l[i-1]:
            cnt+=1
    else:
        if l[i]<l[i+1]:
            cnt+=1
