t=int(input())
for r in range(t):
    n,k,s=input().split()
    if (int(k)+int(s)-1)%int(n)!=0:
        print((int(k)+int(s)-1)%int(n))
    else:
        print(int(n))
