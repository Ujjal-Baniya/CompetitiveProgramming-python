n = int(input())
l =[int(x)/100 for x in input().split()]
x = (sum(l)/n)*100
print(f"{x:.12f}")