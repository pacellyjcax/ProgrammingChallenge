def t(lm,lp):
    mt = [x for x in lm]
    c = 0
    for e in lp:
        if mt.count(lm[e-1])>=1:            
            mt.remove(lm[e-1])
        c+=lm[e-1]
        if len(mt)==0:
            return [c,mt]
    return [c,mt]

while 1:
    try:
        raw_input()
        m = [int(x)for x in raw_input().split()]
        p = [int(x)for x in raw_input().split()]
        st = t(m,p)
        tt = st[0]
        mnt = st[1]
        if len(mnt)>=1:
            print -1
        else:
            print tt
    except:
        break
