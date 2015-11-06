res = [int(raw_input())]
for i in range(9):
    res.append(res[-1]*2)    
for i in range(len(res)):
    print "[N{0:d}] = {1:d}".format(i,res[i])
  
