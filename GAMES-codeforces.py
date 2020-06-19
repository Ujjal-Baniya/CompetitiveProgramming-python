#Date 6/19/2020
#GAMES
n = int(input())
cnt = 0
hm = [None]*n
gu = [None]*n
for i in range(n):
    hm[i], gu[i] = [int(x) for x in input().split()]
for i in range(n):
    for j in range(n):
        if hm[i]==gu[j]:
            cnt+=1
print(cnt)