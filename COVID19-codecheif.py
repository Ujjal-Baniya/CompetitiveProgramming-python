t=int(input())
for r in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    x = []
    v = 0
    for i in range(len(l)):
        if i==len(l)-1:
            x.append(v)
            break
        if l[i+1]-l[i]<=2:
            v+=1
        else:
            x.append(v)
            v=0
    print(min(x)+1,max(x)+1)
