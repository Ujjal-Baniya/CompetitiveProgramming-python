#Distribute Candies
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort(reverse=True)
    s = 0
    for i in range(2,n,3):
        s+=l[i]
    print(s)