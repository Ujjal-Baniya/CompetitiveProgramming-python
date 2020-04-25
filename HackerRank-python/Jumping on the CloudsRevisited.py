n , k = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
final=100
fk=[l[x] for x in range(0,n,k)]
for j in range(0,len(fk)):
    if j==len(fk)-1:
        final=final-1
    else:
        if fk[j+1]==1:
            final=final-3
        else:
            final=final-1
print(final)