d = []
while 1:
    e= int(raw_input())
    if e <0:
        break
    d.append(e)
print "%.2f" % (float(sum(d))/len(d))
