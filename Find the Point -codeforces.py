#Find the Point

t = int(input())
for _ in range(t):
    x1, x2, x3, x4 = [int(x) for x in input().split()]
    print(2*x3-x1,2*x4-x2)