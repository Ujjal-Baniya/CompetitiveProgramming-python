# cook your dish here
def lol(m,Tc,Th):
    for _ in range(m):
        Tc += 1
        Th -= 2
        if Tc==Th:
            return "NO"
    return "YES"
t = int(input())
for _ in range(t):
    m, Tc, Th = [int(x) for x in input().split()]
    print(lol(m,Tc,Th))