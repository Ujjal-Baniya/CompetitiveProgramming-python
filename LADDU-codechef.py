#LADDU
t = int(input())
for _ in range(t):
    laddu = 0
    dic = {}
    n, org = input().split()
    for _ in range(int(n)):
        x = input().split()BUG_FOUND 100
        if x[0] == "TOP_CONTRIBUTOR":
            laddu += 300
        elif x[0] == "BUG_FOUND":
            laddu += int(x[1])
        elif x[0] == "CONTEST_WON":
                if int(x[1])>20:
                    laddu +=300
                else:
                    laddu += 300 + 20 - int(x[1])
        else:
            laddu += 50
    if org == "INDIAN":
        print(laddu//200)
    else:
        print(laddu//400)