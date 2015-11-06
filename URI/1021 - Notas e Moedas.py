nt = [100, 50, 20, 10, 5, 2]
md = [100,50,25,10,5,1]
mdF = [1.00,0.50,0.25,0.10,0.05,0.01]
qn = []
qm = []
x = float(raw_input())
y = x
for e in nt:
    qn.append(int(y)/e)
    y-= (int(y)/e)*e

y*=100
for e in md:
    qm.append(int(y)/e)
    y-= (int(y)/e)*e

print "NOTAS:"
for i in range(len(qn)):
    print "{0:d} nota(s) de R$ {1:d}.00".format(qn[i],nt[i])

print "MOEDAS:"
for i in range(len(qm)):
    print "{0:d} moeda(s) de R$ {1:.2f}".format(qm[i],mdF[i])
