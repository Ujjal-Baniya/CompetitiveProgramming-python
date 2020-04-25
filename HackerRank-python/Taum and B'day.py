for _ in range(int(input())):
    b,w = [int(x) for x in input().split()]
    bc,wc,c=[int(x) for x in input().split()]
    if bc>wc+c:
        bc=wc+c
    elif wc>bc+c:
        wc=bc+c
    print(b*bc+w*wc)   
