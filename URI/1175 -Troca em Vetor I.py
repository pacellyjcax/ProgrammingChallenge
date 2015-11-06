res = [int(raw_input()) for i in range(20)]
res.reverse()


for i in range(len(res)):
    print "N[{0:d}] = {1:d}".format(i,res[i])
     
