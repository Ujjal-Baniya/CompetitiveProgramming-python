#Short Substrings
n = int(input())
for _ in range(n):
    s = input()
    r = s[0]
    for i in range(1,len(s),2):
        r = r+s[i]
    print(r)