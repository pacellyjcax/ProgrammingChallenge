en = [float(raw_input()) for i in range(6)]
vp = 0
vc = 0
for i in range(6):
    if en[i]>0:
        vp+=en[i]
        vc+=1
print str(vc)+" valores positivos"
print "{0:.1f}".format(vp/vc)
