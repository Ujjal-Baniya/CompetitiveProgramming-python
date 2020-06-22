#FCTRL
t = int(input())
for _ in range(t):
    n = int(input())
    i = 5
    c = 0
    while(i<=n):
        c+=n/i
        i=i*5
    print(c)