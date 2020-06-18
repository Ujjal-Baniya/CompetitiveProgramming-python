#Vanya and Fence
n, h = [int(c) for c in input().split()]
l = list(map(int,input().split()))
cnt = 0
for i in range(len(l)):
    if l[i]>h:
        cnt += 2
    else:
        cnt+=1
print(cnt)