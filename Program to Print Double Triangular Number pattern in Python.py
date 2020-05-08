n = int(input())
num = 1
s = ""
for i in range(0, n): 
    num = 1
    for j in range(0, i+1): 
        s = s + str(num)
        num = num + 1
    print(s,end="")
    print((n-int(s[len(s)-1]))*" ",end="")
    print(s[::-1])
    s=""