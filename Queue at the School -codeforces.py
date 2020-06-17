  #Queue at the School
n, t = [int(x) for x in input().split()] #BGGBG --> GBGBG --> GBGGB
queue = input()                          
l = list()
for each in queue:
    l.append(each)
for i in range(t):
    j = 0 
    while j<n-1:
        print(l[j])
        if l[j]=="B" and l[j+1] == "G":
            l[j] = "G"
            l[j+1] = "B"
            j+=1
        j+=1
for each in l:
    print(each,end='')