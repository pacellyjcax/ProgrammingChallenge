def calcula(lc,lp):
    d = {}
    for i in range(len(lc)):
        for k in range(len(lp)):
            j = lc[i].index(k+1)
            if d.has_key(j+1):
                d[j+1] += lp[k]
            else:
                d[j+1] = lp[k]             
                
    pc = max(d.values())
    r = []
    for k in d.keys():
        if d[k] == pc:
            r.append(k)
    return r

res = []
while 1:
    n = raw_input()
    if n == "0 0":
        break
    en = [int(x) for x in n.split()]
    cl = []
    for i in range(en[0]):
        cl.append([int(x) for x in raw_input().split()])

    en = int(raw_input())
    pon = []
    for i in range(en):
        pon.append([int(x) for x in raw_input().split()])
    for e in pon:
        e.pop(0)
    for e in pon:
        res.append(calcula(cl,e))

for e in res:
    if len(e)>1:
        e.sort()
        for i in range(len(e)):
            if i == len(e)-1:
                print e[i]
            else:
                print e[i],
    else:
        print e[0]
