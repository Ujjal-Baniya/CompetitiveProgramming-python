t=int(input())
for x in range(t):
    n,k = input().split()
    l = [int(x) for x in input().split() if int(x)<=0]
    if len(l)>=int(k):
        print("NO")
    else:
        print("YES")
