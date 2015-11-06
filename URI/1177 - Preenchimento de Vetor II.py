f = 0
n= int(raw_input())
for i in range(1000):
    print "N[{0:d}] = {1:d}".format(i,f)
    if f == n-1:
        f = 0
    else:
        f+=1               
