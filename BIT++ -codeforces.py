#BIT++
x = 0
t = int(input())
for _ in range(t):
    case = input()
    if case=="++X" or case=="X++":
        x+=1
    else:
        x-=1
print(x)