#Soldier and Bananas
k, n, w = [int(x) for x in input().split()]
s = 0
for i in range(1,w+1):
    s+=i*k
if s<n:
    print("0")
else:
    print(s-n)