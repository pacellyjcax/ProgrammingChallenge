s = 1
j = 1
for i in range(3,40,2):
    s+=float(i)/(j*2)
    j*=2

print "%.2f" % (s)
