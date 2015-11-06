def ehValido(s):
    for e in s:
        if s.count(e)>1:
            return False
    return True

res = []
while 1:
    try:
        en = [int(x) for x in raw_input().split()]
        qt = 0
        for i in range(en[0],en[1]+1):
            if ehValido(str(i)):
                qt += 1
        res.append(qt)
    except:
        break

for e in res:
    print e
