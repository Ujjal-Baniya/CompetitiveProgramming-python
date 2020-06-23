#Ish and String Game
t = int(input())
for _ in range(t):
    a =  input()
    b = input()
    s = ""
    for i in a:
        if i in b:
            continue
        else:
            s += i
    print(s)