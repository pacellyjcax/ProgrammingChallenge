v = []
for i in xrange(int(raw_input())):
    da = raw_input().split()
    if sum([int(x)for x in raw_input().split()])%2 == 0:
        if da[1] == "PAR":
            v.append(da[0])
        else:
            v.append(da[2])
    else:
        if da[1] == "PAR":
            v.append(da[2])
        else:
            v.append(da[0])

for e in v:
    print e
    
