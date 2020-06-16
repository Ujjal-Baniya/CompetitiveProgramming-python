#WRONG SUBSTRACTION
n, k = input().split()
for _ in range(int(k)):
    if n[len(n)-1]=="0":
        n = str(int(int(n)/10))
    else:
        n = str(int(n)-1)
print(n)