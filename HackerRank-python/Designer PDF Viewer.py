l = [int(x) for x in input().split()]
st="abcdefghijklmnopqrstuvwxyz"
dic={}
i=0
for each in st:
    dic[each]=l[i]
    i+=1
st=input()
final=1
l=[]
for each in st:
    l.append(dic[each])
print(max(l)*len(l))
