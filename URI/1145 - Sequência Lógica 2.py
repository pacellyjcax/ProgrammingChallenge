en = [int(x) for x in raw_input().split()]
res = []
for i in range(1,en[1], en[0]):
    s = ""
    for j in range(i,i+en[0]):
        if j == i+en[0]-1:
            s += str(j)
        else:
            s += str(j)+" "
    res.append(s)
for e in res:
    print e
