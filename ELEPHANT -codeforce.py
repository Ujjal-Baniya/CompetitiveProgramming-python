#ELEPHANT
n = int(input())
# step = 0
# if n%5>=0:
#     step+=int(n/5)
#     n = n%5
#     if n%4>=0:
#         step+=int(n/4)
#         n=n%4
#         if n%3>=0:
#             step+=int(n/3)
#             n = n%3
#             if n%2>=0:
#                 step+=int(n/2)
#                 n = n%2
#                 if n%1>=0:
#                     step+=int(n/1)
# print(step)

#Simplified
n = int(input())
if n%5==0:
    print(int(n/5))
else:
    print(int(n/5)+1)