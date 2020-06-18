#HULK
s1 = "I hate"
s2 = "I love"
s = s1
n = int(input())
for i in range(n-1):
    if i%2==0:
        s+=" that " + s2
    else:
        s+=" that " + s1
print(s+" it")