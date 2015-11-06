nt = [100, 50, 20, 10, 5, 2 , 1]
qc = []
x = int(raw_input())
y = x
for e in nt:
    qc.append(y/e)
    y-= (y/e)*e

print x
for i in range(len(qc)):
    print "{0:d} nota(s) de R$ {1:d},00".format(qc[i],nt[i])
