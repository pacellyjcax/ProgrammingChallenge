res = []
while 1:
    n = [int(x) for x in raw_input().split()]
    if n[0] == 0 and n[1]==0:
        break
    lm = [int(raw_input()) for i in xrange(n[0])]
    nt = [int(raw_input()) for i in xrange(n[1])]
    r = []
    for e in nt:
        if lm.count(e)>=1:
            r.append([e,lm.index(e)])
        else:
            r.append([e,-1])
    res.append(r) 
    
for i in xrange(len(res)):
    print "CASE# %d:"%(i+1)
    for f in res[i]:
        if f[1] == -1:
            print f[0]," not found"
        else:
            print f[0], " found at ", f[1]
        
            
