res = []
n = int(raw_input())
for i in xrange(n):
    raw_input()
    nts = [int(x) for x in raw_input().split()]
    ntsf = [x for x in nts]
    ntsf.sort(reverse=True)
    c = 0
    for i in xrange(len(nts)):
        if nts[i] == ntsf[i]:
            c+=1
    res.append(c)
    
for e in res:
    print e
            
