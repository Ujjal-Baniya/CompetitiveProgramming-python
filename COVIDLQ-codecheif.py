t = int(input())
for b in range(t):
    n=int(input())
    l=[int(x) for x in input().split()]
    flag=0
    index=l.index(1)
    for i in range(l.index(1)+1,n):
        if l[i]==1:
            a=i-index
            if a<6:
                flag=1
            index=i
    if(flag):
        print("NO")
    else:
        print("YES")