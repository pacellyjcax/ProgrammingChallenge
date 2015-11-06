def cont(s):
    a = s.split()
    ls = [x[0] for x in a]
    t = 0
    checa = True
    for i in xrange(len(ls)-1):
        if ls[i] == ls[(i+1)] and checa:
            t+=1
            checa = False
        else:
            checa = True    
    return t

while 1:
    try:
        print cont(raw_input().lower())
    except:
        break
