n,k = input().split()
l = [int(x) for x in input().split()]
total_paid = int(input())
to_pay = (sum(l)-l[int(k)])/2
owe = total_paid - to_pay
if owe == 0:
    print("Bon Appetit")
else:
    print(int(owe))