res = []
for i in range(100):
    res.append(float(raw_input()))    

for i in range(len(res)):
    if res[i]<=10:
        if int(str(res[i]).split(".")[1])==0:
            print "A[{0:d}] = {1:s}".format(i,str(res[i]).split(".")[0])
        else:
            print "A[{0:d}] = {1:s}".format(i,str(res[i]))
  
