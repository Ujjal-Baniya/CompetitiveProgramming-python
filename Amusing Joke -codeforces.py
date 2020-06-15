#Amusing Joke
from collections import Counter
s = input()
r = input()
m = input()
if Counter(s)+Counter(r)==Counter(m):
    print("YES")
else:
    print("NO")