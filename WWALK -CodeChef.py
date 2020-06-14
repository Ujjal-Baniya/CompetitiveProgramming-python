#WWALK
t = int(input())
for _ in range(t):
    n =int(input())
    l = list(map(int,input().split()))
    m = list(map(int,input().split()))
    s1 = 0
    s2 = 0
    main = 0
    for i in range(n):
        try:
            if s1==s2 and l[i]==m[i]:
                 main+=l[i]
        except:
            pass
    print(main)