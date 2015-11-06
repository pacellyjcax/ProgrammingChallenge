
res = []
for i in range(int(raw_input())):
    
    en = [int(x) for x in raw_input().split()]
    posX = [x for x in range(en[0],en[2]+1)]
    posY = [y for y in range(en[1],en[-3]+1)]
    if posX.count(en[-2])==1 and posY.count(en[-1])==1:
        res.append(1)
    else:
        res.append(0)
for e in res:
    print e
