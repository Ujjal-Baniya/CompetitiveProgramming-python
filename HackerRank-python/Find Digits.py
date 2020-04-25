t=int(input())
for i in range(t):
    x =input()
    count=0
    for j in range(len(x)):
        if int(x[j])==0:
            continue
        elif int(x)%int(x[j])==0:
            count+=1
    print(count)
