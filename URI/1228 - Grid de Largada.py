def calculaUltrapassagens(l,lc):
    tu = 0
    for i in range(len(lc)):
        ults = lc.index(l[i])-i
        if ults > 0:
            tu+=ults  
    return tu

def conta(ll,lc):
    t = 0
    for i in range(len(lc)):
        pf = lc.index(lc[i])
        pi = ll.index(lc[i])
        if pf < pi:
            t += pi-pf
    return t
def contaU(li,lf):
    d = {}
    for i in range(len(li)):
        if i < len(li):
            d[li[i]] = [li[x] for x in range(i+1,len(li))]
        else:
            d[li[i]] = []
    df = {}
    for i in range(len(lf)):
        if i < len(lf):
            df[lf[i]] = [lf[x] for x in range(i+1,len(lf))]
        else:
            df[lf[i]] = []
    for e in lf:
        for k in d[e]:
            try:
                df[e].remove(k)
            except:
                continue
    return sum([len(x) for x in d.values()])

print calculaUltrapassagens([1,2, 3, 4, 5],[3, 1, 2, 5, 4])
print calculaUltrapassagens([3, 1, 2, 5, 4],[1, 2, 3, 4, 5])
print calculaUltrapassagens([3, 1, 2, 5, 4],[5, 3, 2, 1, 4])
print conta([1,2, 3, 4, 5],[3, 1, 2, 5, 4])
print conta([3, 1, 2, 5, 4],[1, 2, 3, 4, 5])
print conta([3, 1, 2, 5, 4],[5, 3, 2, 1, 4])
print contaU([1,2, 3, 4, 5],[3, 1, 2, 5, 4])
print contaU([3, 1, 2, 5, 4],[1, 2, 3, 4, 5])
print contaU([3, 1, 2, 5, 4],[5, 3, 2, 1, 4])
'''
res = []
for i in range(int(raw_input())):
    raw_input()
    en = [int(x) for x in raw_input().split()]
    res.append(calculaUltrapassagens(en))

for e in res:
    print "Optimal train swapping takes %d swaps." % e
'''
