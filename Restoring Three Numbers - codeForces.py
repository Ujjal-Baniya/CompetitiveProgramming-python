#Restoring Three Numbers
l = [int(x) for x in input().split()]
ma = max(l)
for each in l:
    if each!=ma:
        print(ma-each,end = " ")