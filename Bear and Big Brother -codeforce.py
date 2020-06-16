#Bear and Big Brother
a, b =[int(x) for x in input().split()]
cnt = 0
while True:
    if a>b:
        break
    a *=3
    b *=2
    cnt+=1
print(cnt)