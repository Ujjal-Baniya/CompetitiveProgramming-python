#day 2
def super_list(l):
    r = []
    for num in l:
        if num%3!=0:
            continue
        else:
            if num>30:
                num+=5
            else:
                num-=5
            r.append(num)
    return r
l =[int(x) for x in input().split()]
print(super_list(set(l)))