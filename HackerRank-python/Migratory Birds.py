n = int(input())
l = [int(x) for x in input().split()]
z = []
for x in range(0,6):
    z.append(l.count(x))
maxx = max(z)
for x in range(0,6):
    if l.count(x)==maxx:
        print(x)
        break