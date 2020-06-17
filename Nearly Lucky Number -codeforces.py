#Nearly Lucky Number
x = input()
s = 0
for i in range(len(x)):
    if x[i]=='4' or x[i]=='7':
        s+=1
if s==4 or s == 7:
    print("YES")
else:
    print("NO")