#OK - Mais legivel
n = int(raw_input())
for i in xrange(n):
    en = raw_input().split()
    print "Case %d:"%(i+1)
    if en[1] == "bin":
        print int(en[0],2),"dec"
        print hex(int(en[0],2))[2:],"hex"
    elif en[1] == "dec":
        print hex(int(en[0]))[2:],"hex"
        print bin(int(en[0]))[2:],"bin"
    elif en[1] == "hex":
        print int(en[0],16),"dec"
        print bin(int(en[0],16))[2:],"bin"
    print

#OK -0.136
'''
n = int(raw_input())
res = []
for i in xrange(n):
    en = raw_input().split()
    if en[1] == "bin":
        res.append([str(int(en[0],2))+" dec",
                    str(hex(int(en[0],2)))[2:]+" hex"])
    elif en[1] == "dec":
        res.append([str(hex(int(en[0])))[2:]+" hex",
                    str(bin(int(en[0])))[2:]+" bin"])
    elif en[1] == "hex":
        res.append([str(int(en[0],16))+" dec",
                    str(bin(int(en[0],16)))[2:]+" bin"])

for i in xrange(len(res)):
    print "Case %d:"%(i+1)
    for el in res[i]:
        print el
    print
'''
