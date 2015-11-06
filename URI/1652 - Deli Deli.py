res = []
e = [int(x) for x in raw_input().split()]
ir = {}
for i in range(e[0]):
    j = [x for x in raw_input().split()]
    ir[j[0]] = j[1]

for i in range(e[1]):
    e = raw_input()
    if ir.has_key(e):
        res.append(ir[e])
    elif e[-1] == "y" and ["a","e","i","o","u"].count(e[-2]) == 0:
        res.append(e[:-1]+"ies")
    elif ["o","s","x"].count(e[-1]) == 1:
        res.append(e+"es")
    elif ["ch","sh"].count(e[-2:]) == 1:
        res.append(e+"es")
    else:
        res.append(e+"s")

for e in res:
    print e
