while 1:
    n = int(raw_input())
    if n == 0:
        break
    c = []
    p = []
    for i in xrange(n):
        m = [int(x) for x in raw_input().split()]
        c.append(m[0])
        p.append(m[1])
    cf = [0 for j in xrange(len(c))]
    if sum(p) == 0:
        for i in xrange(len(c)):
            cf[i+p[i]] = c[i]
        if cf.count(0) >= 1:
            print -1
        else:
            vf = str(cf)
            vf = vf.replace("[","")
            vf = vf.replace("]","")
            vf = vf.replace(",","")
            print vf
    else:
        print -1
