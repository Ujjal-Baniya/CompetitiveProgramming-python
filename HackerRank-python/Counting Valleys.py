n=int(input())
i=list(input())
v=0
l=0
for each in i:
    if each=='U':
        l+=1
    if each=='D':
        l+=-1
    if l==0 and each=='U':
        v+=1
print(v)