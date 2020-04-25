n = int(input())
l = [int(x) for x in input().split()]
count=0
i=0
while i<n:
    count +=1
    if i<n-2 and l[i+2]==0:
        i += 1
    i += 1 
print(count-1) 
