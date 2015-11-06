l = []
while 1:
    K = raw_input()
    if K=='0':
        break
    elif 0 < int(K) <= 10**3:
        NM = raw_input()
        lNM = NM.split()
        N,M = float(lNM[0]),float(lNM[1])
        if -(10**4) < N < (10**4) and -(10**4) < M < (10**4):
            for i in xrange(int(K)):
                XY = raw_input()
                lXY = XY.split()
                X,Y = float(lXY[0]),float(lXY[1])
                if X==N or Y==M:
                    l.append('divisa')
                elif X>N and Y>M:
                    l.append('NE')
                elif X>N and Y<M:
                    l.append('SE')
                elif X<N and Y>M:
                    l.append('NO')
                elif X<N and Y<M:
                    l.append('SO')
for e in l:
    print e
