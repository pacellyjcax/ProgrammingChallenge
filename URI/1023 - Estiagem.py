f = []
while 1:
    n = int(raw_input())
    if n == 0:
        break
    d = [raw_input().split() for i in range(n)]
    lcm = [int(x[1])/int(x[0]) for x in d]
    lc = [int(x[1]) for x in d]
    lp = [int(x[0]) for x in d]
    tc = sum(lc)
    tp = sum([int(x) for x in lp])
    strC = ""
    for i in range(len(d)-1):
        posMin = lcm.index(min(lcm))
        qnt = lcm.count(min(lcm))
        if qnt >1:
            for i in range(qnt-1):
                posM = lcm.index(min(lcm))                
                posM = lcm.index(lcm.pop(posM))
                lp[posMin]+=lp.pop(posM+1)
    for i in range(len(lp)):
        posMin = lcm.index(min(lcm))
        if i == len(d)-1:
            strC += "{0:d}-{1:d}".format(lp.pop(posMin),lcm.pop(posMin)) 
        else:
            strC += "{0:d}-{1:d} ".format(lp.pop(posMin),lcm.pop(posMin))
    cmt = float(tc)/tp
    f.append((strC,cmt))

for i in range(len(f)):
    if i == len(f)-1:
        s = str(f[i][1]).split(".")
        sF = s[0]+"."+s[1][:2]
        print '''Cidade# {0:d}:
{1:.2f}
Consumo medio: {2:s} m3.'''.format(i+1,f[i][0],float(sF))
    else:
        s = str(f[i][1]).split(".")
        sF = s[0]+"."+s[1][:2]
        print '''Cidade# {0:d}:
{1:.2f}
Consumo medio: {2:s} m3.'''.format(i+1,f[i][0],float(sF))
        print
