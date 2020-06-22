#CONFLIP
import math
t  = int(input())
    for _ in range(t):
    g = int(input())
    for _ in range(g):
        i, n, q = [int(x) for x in input().split()]
        if i != q:
            print(math.ceil(n/2))
        else:
            print(n-math.ceil(n/2))