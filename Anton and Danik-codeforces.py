#Anton and Danik
n = int(input())
s = input()
cntA = 0
cntB = 0
for i in range(n):
    if s[i]=="A":
        cntA += 1
    else:
        cntB +=1
if cntA>cntB:
    print("Anton")
elif cntB>cntA:
    print("Danik")
else:
    print("Friendship")