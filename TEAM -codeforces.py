#TEAM
t = int(input())
count = 0
for _ in range(t):
    s = input()
    if s.count('1')>=2:
        count+=1
    else:
        continue
print(count)