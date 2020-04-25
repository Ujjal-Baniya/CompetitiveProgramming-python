n = int(input())
for i in range(n):
    l = [int(x) for x in input().split()]
    a = l[0]-l[2]
    b = l[1]-l[2]
    if abs(a)<abs(b):
        print("Cat A")
    elif abs(b)<abs(a):
        print("Cat B")
    else:
        print("Mouse C")