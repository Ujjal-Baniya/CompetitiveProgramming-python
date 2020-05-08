t = int(input())
for x in range(t):
    n = int(input())
    l = [int(x)%(10**9+7) for x in input().split()]
    l.sort(reverse=True)
    summ=0
    for i in range(n):
        if i!=0:
            val = l[i]-i
            if val>0:
                summ = summ+val
        else:
            summ=summ+l[i]
    print(summ%(10**9+7))