#Counter.OrderedDict
from collections import OrderedDict
dic = dict()
dig = ""
name = ""
n = int(input())
for _ in range(n):
    for each in input():
        if each.isdigit():
            dig = dig+each
        else:
            name = name+each
    try:
        if dic[name[:len(name)-1]]:
            dic[name[:len(name)-1]] = int(dic[name[:len(name)-1]]) + int(dig)
    except:
        dic[name[:len(name)-1]] = dig 
    dig =""
    name = ""
dic = OrderedDict(dic)
for key in dic.keys():
    print(key,dic[key])