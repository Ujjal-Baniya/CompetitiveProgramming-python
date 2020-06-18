#Magnets
n = int(input())
cnt = 0
for i in range(n):
    if i==0:
        prev=int(input())
    else:
        ne = int(input())
        if ne!=prev:
            cnt+=1
        prev = ne
print(cnt+1)
