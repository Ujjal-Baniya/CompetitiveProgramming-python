import collections
a = input().lower()
d = dict(collections.Counter(a))
l = [x for x in d.values()]
for x in set(sorted(l)):
    for y in d.keys():
        if y.isalpha():
            if d[y] == x:
                print(y, end=" ")