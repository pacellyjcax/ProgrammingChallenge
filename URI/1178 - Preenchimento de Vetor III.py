vf = []
x = float(raw_input())
vf.append(x)
for i in range(1,100):
    vf.append(vf[i-1]/2)

for i in range(len(vf)):
    print "N[{0:d}] = {1:.4f}".format(i,vf[i])
