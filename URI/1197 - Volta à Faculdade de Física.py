def calcula(l):
    '''if l[1] == 0:
        return 0
    return float(l[0])/l[1]/2*pow((l[1]*2),2)'''
    return l[0]*(l[1]*2)

res = []
while 1:
    try:
        res.append(calcula([int(x) for x in raw_input().split()]))
    except:
        break

for e in res:
    print int(e)
