#Fox And Snake
n, m = [int(x) for x in input().split()]
event = True
for i in range(n):
    if i%2==0:
        print(m*"#")
    else:
        if event:
            print("."*(m-1) + "#")
            event = False
        else:
            print("#" + "."*(m-1))
            event = True