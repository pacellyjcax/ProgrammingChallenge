n= int(raw_input())
for i in xrange(n):
    e = [int(x) for x in raw_input().split()]
    jog = [1 for x in xrange(e[0])]
    t = {}
    for j in xrange(e[1]):
        et = [int(x) for x in raw_input().split()]
        t[et[0]] = et[1]
    cont = 0
    for j in xrange(e[2]):
        if cont == e[0]:
            cont = 0
        da = int(raw_input())
        if t.has_key(jog[cont]+da):
            jog[cont] = t[jog[cont]+da]
        elif jog[cont]+da > 100:
            jog[cont] = 100
        else:
            jog[cont] += da
        cont += 1
    for j in xrange(len(jog)):
        print "Position of player %d is %d." %((j+1),jog[j])
