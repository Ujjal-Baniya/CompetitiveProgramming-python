#Carvans
t = int(input())
for _ in range(t):
    n = int(input())
    l =list(map(int,input().split()))
    s = 0
    cnt = 0
    for each in l:
        if l.index(each) == 0:
            s = each
            cnt+=1
        if each<s:
            s = each
            cnt+=1
            
    print(cnt)