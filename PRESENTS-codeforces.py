#Presents
n = int(input())
l = [int(x) for x in input().split()]
s = l.copy()
for i in range(n):
    s[l[i]-1] = i+1
for i in range(n):
    print(s[i],end=" ")