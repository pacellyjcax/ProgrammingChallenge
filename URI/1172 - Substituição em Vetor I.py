res = []
for i in range(10):
    d = int(raw_input())
    if d<=0:
        res.append(1)
    else:
        res.append(d)
    
for i in range(len(res)):
    print "X[{0:d}] = {1:d}".format(i,res[i])
  
