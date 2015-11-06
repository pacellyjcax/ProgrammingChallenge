i = 0.0
while i <= 2.0:
    for j in [1,2,3]:
        if str(i).strip()[-1] == "0":
            print "I={0:.0f} J={1:d}".format(i,int(j+i))
        else:
            print "I={0:.1f} J={1:.1f}".format(i,j+i)
    i+=0.2
