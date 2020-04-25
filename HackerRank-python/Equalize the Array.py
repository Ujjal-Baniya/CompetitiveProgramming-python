n = int(input())
l = [int(x) for x in input().split()]
from collections import Counter
d=Counter(l).values()
deletion=len(l)-max(d)
print(deletion)
