#TRAM
t = int(input())
maxCapacity = 0
currentCapacity = 0
for _ in range(t):
    b, a = [int(c) for c in input().split()]
    currentCapacity+= a - b
    if currentCapacity > maxCapacity:
        maxCapacity = currentCapacity
print(maxCapacity)