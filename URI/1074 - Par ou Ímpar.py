r = []
n = int(raw_input())
en = [int(raw_input()) for i in range(n)]
par = [x for x in en if x%2==0]
imp = [x for x in en if x%2>0]
pos = [x for x in en if x>0]
neg = [x for x in en if x<0]

for e in en:
    sf = ""
    if e == 0:
        sf+="NULL"
    else:
        if par.count(e)>0:
            sf+="EVEN"
        elif imp.count(e)>0:
            sf+="ODD"
        if pos.count(e)>0:
            sf+=" POSITIVE"
        elif neg.count(e)>0:
            sf+=" NEGATIVE"
    r.append(sf)

for e in r:
    print e
