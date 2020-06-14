t = int(input())
for _ in range(t):
    l = [int(x) for x in input().split()]
    if sum(l[5]*l[:5])<=120:
        print("No")
    else:
        print("Yes")