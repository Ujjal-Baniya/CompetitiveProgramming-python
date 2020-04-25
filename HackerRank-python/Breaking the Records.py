x = int(input())
high = 0
low = 0
a = [int(x) for x in input().split()]
hs=lo=a[0]
for ne in a:
    if ne>hs:
        hs = ne
        high+=1
    if ne<lo:
        low+=1
        lo = ne
print(high,low)