#CONVSTR
st = input()
ch = input()
for each in set(ch):
    if each not in set(st):
        print("-1")
        break