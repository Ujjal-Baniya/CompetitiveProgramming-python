n=int(input())
l=[int(x) for x in input().split()]
for i in range(n):
    a=l.index(i+1)
    b=l.index(a+1)
    print(b+1)
