#EOEO
count = 0
flag = 1
ts = int(input())
if ts%2!=0:
    for each in range(1,ts):
        if each%2==0:
            count+=1
        else:
            continue
    print(count)
else:
    print(count)