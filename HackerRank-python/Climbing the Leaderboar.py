n = int(input())
r = [int(x) for x in input().split()]
m = int(input())
s = [int(x) for x in input().split()]

while(s):
    count = 0
    rank = s[0]
    r.append(rank)
    r=list(set(r))
    r.sort(reverse=True)
    for each in r:
        count+=1
        if each==rank:
            print(count)
    s.remove(rank)
