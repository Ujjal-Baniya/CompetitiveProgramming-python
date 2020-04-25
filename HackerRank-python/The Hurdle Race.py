n,m = input().split()
l=[int(x) for x in input().split()]
a = max(l)
if a-int(m)>0:
    print(a-int(m))
else:
    print(0)
