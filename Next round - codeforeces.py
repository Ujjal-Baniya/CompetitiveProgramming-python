n, r = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
count = 0
for i in range(n):
    if l[i]>0 and l[i]>=l[r-1]:
        count+=1
print(count)