#C+=
t = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    x = 0
    while l[0] <= l[2] and l[1] <= l[2]:
        x+=1
        if l[0]<l[1]:
            l[0]+=l[1]
        else:
            l[1]+=l[0]
    print(x)