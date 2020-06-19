#Divisibility Problem
t = int(input())
for _ in range(n):
    a, b =[int(x) for x in input().split()]
    num = a/b
    if num - int(num):
        print((int(num)+1)*b-a)
    else:
        print(0)