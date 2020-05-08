from collections import Counter
r = int(input())
for xx in range(r):
    x,n=[int(x) for x in input().split()]
    s = input()
    x = dict(Counter(s))
    for xxx in range(n):
        iso = int(input())
        g = 0
        for each in x.values():
            if each>iso:
                g=g+each-iso
        print(g)