import math
res = []
for i in range(int(raw_input())):
    en = int(raw_input())
    res.append(math.ceil(float(en)/1.6129032258064516129032258064516))
for e in res:
    print e
