n = int(input())
l = [int(x) for x in input().split()]
l.sort()
s=list(set(l))
s.sort()
while(s):
    count=0
    for i in range(n):
        if l[i]-s[0]>=0:
            count+=1
    print(count)
    s.remove(s[0])
