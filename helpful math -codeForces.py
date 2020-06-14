#helpful math
x = input()
l = [int(r) for r in x if r!="+"]
l = sorted(l)
for i in range(len(l)):
    if i == len(l)-1:
        print(l[i])
    else:
        print(l[i],end='+')