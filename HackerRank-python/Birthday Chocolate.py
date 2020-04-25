n = int(input())
l = [int(x) for x in input().split()]
d,m=[int(x) for x in input().split()]
i=0
count=0
while(True):
    if m==len(l)+1:
        break
    x=l[i:m]
    if sum(x)==d:
        count+=1
    i+=1
    m+=1
print(count)