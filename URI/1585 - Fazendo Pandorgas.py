res = []
for i in range(int(raw_input())):
    en = [float(x) for x in raw_input().split()]
    res.append("%d cm2" % (int((en[0]*en[1])/2)))
 
for e in res:
    print e
