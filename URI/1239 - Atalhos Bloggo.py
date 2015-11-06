def ita(op):
    if op%2 ==0:
        return "<i>"
    return "</i>"
def neg(op):
    if op%2 ==0:
        return "<b>"
    return "</b>"
        

res = []
while 1:
    try:
        d = raw_input()
        opi = 1
        opn = 1
        r = ""
        for i in range(len(d)):
            if d[i] == "_":
                opi+=1
                r += ita(opi)
            elif d[i] == "*":
                opn+=1
                r += neg(opn)
            else:
                r += d[i]
        res.append(r)
    except:
        break
    
for e in res:
    print e
