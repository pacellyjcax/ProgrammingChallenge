while 1:
    en = raw_input()
    if (en == "0 0 0 0"):
        break
    
    t = [int(x) for x in en.split()]
    hi = t[0]
    mi = t[1]
    hf = t[2]
    mf = t[3]
    ts = 0
    
    if hi<=hf:
        ts=(hf-hi)*60
    else:
        ts=(24-(hi-hf))*60

    if mi<=mf:
        ts+=mf-mi;
    else:
        ts+=60-60-mi+mf

    if hi==hf and mi>mf:
        ts=23*60+(60-mi+mf)

    print ts
'''
def calcula(hi,mi,hf,t[3]):
    ti = (hi*3600)+(mi*60)
    tf = (hf*3600)+(mf*60)
    if hi>=hf and not hf == 0:
        return((86400-ti)+tf)/60
    else:
        if hf == 0:
            #86400 equivale ao dia em segundos
            return((86400-ti)+tf)/60
    return (tf - ti)/60
res = []
while 1:
    e = raw_input()
    if e == "0 0 0 0":
        break
    l = [int(x) for x in e.split()]
    t = calcula(l[0],l[1],l[2],l[3])

    res.append(t)
 
for e in res:
    print e





'''
#runtime error por uso de biblioteca e por nao emitir
#saida na sequencia da entrada
'''
import datetime
 
res = []
while 1:
    e = raw_input()
    if e == "0 0 0 0":
        break
    l = [int(x) for x in e.split()]
    d1 = datetime.datetime(day=13, month=2, year=1988,hour=l[0],minute=l[1])
    d2 = datetime.datetime(day=13, month=2, year=1988,hour=l[2],minute=l[3])
    if l[2]<l[0]:
        d2 = datetime.datetime(day=14, month=2, year=1988,hour=l[2],minute=l[3])
    diff = d2-d1
    res.append((diff.seconds/60))
 
for e in res:
    print e

'''


