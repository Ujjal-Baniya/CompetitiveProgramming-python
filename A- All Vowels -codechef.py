#A - All Vowels

vowel = "aeiou"
t = int(input())
for _ in range(t):
    cnt = 0
    n = input()
    for each in n:
        if each in vowel:
            continue
        else:
            x = abs(ord(each)-96 - 1)
            y = abs(ord(each)-96 - 5)
            w = abs(ord(each)-96 - 9)
            z = abs(ord(each)-96 - 15)
            a = abs(ord(each)-96 - 21)
            cnt+= min(x,y,w,z,a)
    print(cnt)