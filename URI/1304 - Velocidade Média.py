import datetime
def dist(l1,l2,v):
    d1 = datetime.datetime(day=13, month=2, year=2015, hour=l1[0], minute=l1[1],second=l1[2])
    d2 = datetime.datetime(day=13, month=2, year=2015, hour=l2[0], minute=l2[1],second=l2[2])
    diff = d2-d1
    return ((v/60.0)/60.0)*diff.seconds

ti = []
v = 0
d = 0
tf = []
while 1:
    try:
        e= raw_input().split()
        if len(e) == 2:
            ti = [int(x) for x in e[0].split(":")]
            if len(tf) >0:
                d += dist(tf,ti,v)
            v = float(e[1])
        else:        
            tf = [int(x) for x in e[0].split(":")]
            d+=dist(ti,tf,v)
            print e[0]+" %.2f km" %(d)
            ti = [x for x in tf]
    except:
        break
