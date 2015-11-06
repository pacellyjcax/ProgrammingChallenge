e = [float(X) for X in raw_input().split()]

if e[0]>0:
    if e[1]>0:
        print "Q1"
    elif e[1]<0:
        print "Q4"
    else:
        print "Eixo X"
elif e[0]<0:
    if e[1]>0:
        print "Q2"
    elif e[1]<0:
        print "Q3"
    else:
        print "Eixo X"
else:
    if e[1]==0:
        print "Origem"
    else:
        print "Eixo Y"
    

