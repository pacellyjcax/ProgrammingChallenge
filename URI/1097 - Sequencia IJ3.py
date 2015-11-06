vi = 5
for i in range(1,10,2):
    ls =[x for x in range(vi,vi+3)]
    ls.reverse()
    for j in ls:
        print "I={0:d} J={1:d}".format(i,j)
    vi+=2
