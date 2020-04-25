n = int(input())
k = int(input())
def solution(n,p):
    pages = int(n/2)
    right = int(p/2)
    left = pages-right
    if(right<left):
        return right
    else:
        return left
x = solution(n,k)
print(x)