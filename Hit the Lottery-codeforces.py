#Hit the Lottery
n = int(input())
l = [100, 20, 10, 5, 1]
step = 0
for each in l:
    if n%each!=n:
        step+= n//each
        n = n%each
print(step)