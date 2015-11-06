res =[]
while 1:
    en = int(raw_input())
    if en == 0:
        break
    da = [int(X) for X in range(1,en+1)]
    dis = []
    while len(da)>=2:
        dis.append(da.pop(0))
        da.append(da.pop(0))

    res.append('''Discarded cards: {0:s}
Remaining card: {1:d}'''.format(str(dis)[1:-1],da[0]))
    
for e in res:
    print e
