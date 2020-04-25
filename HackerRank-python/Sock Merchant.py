n = int(input())
l = [int(x) for x in input().split()]
s =list()
prev = 0
l.sort()
for each in l:
    if each != prev:
        s.append(l.count(each))
    prev = each
total = 0
for each in s:
    total = total + each//2
print(total)