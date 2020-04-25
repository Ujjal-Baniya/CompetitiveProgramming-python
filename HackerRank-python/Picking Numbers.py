n = int(input())
l = [int(x) for x in input().split()]
dic =dict()
a =list()
l.sort()
for i in range(n):
    a.append(l[i])
    for j in range(i+1,n):
        if abs(l[i]-l[j])<2:
            a.append(l[j])
            dic[i]=a
    a=[]
l=[]
for z in dic.values():
    l.append(len(z))
print(max(l))
