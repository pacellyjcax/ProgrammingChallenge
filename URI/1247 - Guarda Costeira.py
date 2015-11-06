import math

def pega(D,VF,VG):
    dist = math.sqrt(pow(12,2) + pow(D,2))
    tf = 12.0 / VF
    tg = dist / VG        
    if tf >= tg:
        return True
    return False
        
res = []
while 1:
    try:
        en = [float(x) for x in raw_input().split()]
        if pega(en[0],en[1],en[2]):
            res.append("S")
        else:
            res.append("N")
    except:
        break
    
for e in res:
    print e
