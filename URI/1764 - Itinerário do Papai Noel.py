from operator import itemgetter

def cobMin(g,qt):
    nV = []
    t = 0    
    for e in sorted( g, key=itemgetter(2) ):
        va = False
        if nV.count(e[0]) == 0:
            nV.append(e[0])
            va = True
        if nV.count(e[1]) == 0:
            nV.append(e[1])
            va = True
        if va:
            t+=e[2]
    return t

while 1:
    en = [int(k) for k in raw_input().split()]
    if sum(en) == 0:
        break
    g = []
    for i in xrange(en[1]):
        da = [int(k) for k in raw_input().split()]
        g.append((da[0],da[1],da[2]))
    print cobMin(g,en[0])
