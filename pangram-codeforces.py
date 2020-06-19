#pangram
n = int(input())
if len(set(input().lower()))==26:
    print("YES")
else:
    print("NO")