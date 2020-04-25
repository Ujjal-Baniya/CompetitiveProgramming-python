a,b,k=input().split()
count=0
x = [str(v) for v in range(int(a),int(b)+1)]
y = [v[::-1] for v in x]
for first,second in zip(x,y):
    if abs(int(first)-int(second))%int(k)==0:
        count+=1
print(count)
