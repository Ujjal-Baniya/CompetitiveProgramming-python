n,k = input().split()
l = [int(x) for x in input().split()]
count =0
for i in range(int(n)): 
    for j in range(i+1,int(n)):
        try:
            summ = l[i]
            summ = summ + l[j]
            if summ%int(k) == 0:
                count+=1
        except:
            continue
print(count)