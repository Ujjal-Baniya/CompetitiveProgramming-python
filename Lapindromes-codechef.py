#Lapindromes
t = int(input())
for _ in range(t):
    s = input()
    if len(s)%2==0:
        if sorted(s[:int(len(n)/2)]) == sorted(s[int(len(n)/2):]):
            print("YES")
        else:
            print("NO")
    else:
        if sorted(s[:int(len(n)/2)]) == sorted(s[int(len(n)/2)+1:]):
            print("YES")
        else:
            print("NO")