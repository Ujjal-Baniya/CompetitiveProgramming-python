b,n,m =input().split()
key = [int(x) for x in input().split()]
usb = [int(x) for x in input().split()]
lis=list()
for a in key:
    for d in usb:
        price = a + d
        if price <= int(b):
            lis.append(price)
        else:
            continue
lis.sort()
if(len(lis)):
    print(max(lis))
else:
    print(-1)