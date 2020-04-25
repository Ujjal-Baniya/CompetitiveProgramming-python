n,k,q=[int(n) for n in input().split()]
l=[int(x) for x in input().split()]
while(k):
    l.insert(0,l.pop())
    k=k-1
for i in range(q):
    x=int(input())
    print(l[x])
