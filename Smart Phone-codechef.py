#Smart Phone
t = int(input())
l = []
for _ in range(t):
    n = int(input())
    l.append(n)
l = sorted(l)
maX = 0
for i in range(t):
    if maX < l[i]*(t-i):
        maX = l[i]*(t-i)
print(maX)