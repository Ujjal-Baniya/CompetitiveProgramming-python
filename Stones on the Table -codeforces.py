#Stones on the Table
n = int(input())
l = input()
count = 0
for i in range(len(l)):
    try:
        if l[i]==l[i+1]:
            count+=1
    except:
        break
print(count)