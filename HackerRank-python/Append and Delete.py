s = input()
t = input()
k=int(input())
flag=0
while(k):
    if len(s)==0:
        k=k-len(t)
        if k>=0:
            flag=1
            break
        else:
            break
    elif s in t:
        if s[0]==t[0]:
            if len(t)-len(s)==k:
                flag=1
                break
            elif len(t)-len(s)<k:
                if len(s)%2==len(t)%2: 
                    if k%2==0:
                        flag=1
                else:
                    if k%2!=0:
                        flag=1
            else:
                break
    s=s[:-1]
    k-=1
if flag==0:
       print('No')
else:
    print('Yes')
