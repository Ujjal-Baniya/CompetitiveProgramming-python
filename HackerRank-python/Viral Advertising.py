n=int(input())
share=5
like=2
for i in range(2,n+1):
    share=(share//2)*3
    like=like+share//2
print(like)
