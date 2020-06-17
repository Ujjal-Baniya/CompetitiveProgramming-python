#George and Accommodation
n = int(input())
cnt = 0
for _ in range(n):
    o, t = [int(x) for x in input().split()]
    if t-o>=2:
        cnt +=1
print(cnt)