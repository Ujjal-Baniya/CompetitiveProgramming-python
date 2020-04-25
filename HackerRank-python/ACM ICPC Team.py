n,k = [int(x) for x in input().split()]
l=[]
b=[]
for i in range(n):
    l=input()
    b.append(l)
    l=[]
maxx=0
for i in range(len(b)):
    for j in range(i+1,len(b)):
        try:
            x = list(bin(int(b[i],2) | int(b[j],2)))
            if maxx <= x.count('1'):
                l.append(x.count('1'))
                maxx=x.count('1')
        except:
            continue
print(maxx)
print(l.count(maxx))
