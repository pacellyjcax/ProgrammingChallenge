import fractions

def ehPitagorica(l):
    if pow(l[2],2) == pow(l[0],2)+pow(l[1],2):
        return True
    return False

def mdc(l):
    return fractions.gcd(fractions.gcd(l[0],l[1]),l[2])

res = []
while 1:
    try:
        en = [int(x) for x in raw_input().split()]
        en.sort()
        if ehPitagorica(en):
            if mdc(en) == 1:
                res.append("tripla pitagorica primitiva")
            else:
                res.append("tripla pitagorica")
        else:
            res.append("tripla")
    except:
        break
    
for e in res:
    print e
