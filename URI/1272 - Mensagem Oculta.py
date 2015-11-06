e= int(raw_input())
res = []
for i in xrange(e):
    d = raw_input()
    res.append("".join([x[0] for x in d.split() if x.isalpha()]))
    
for e in res:
    print e


