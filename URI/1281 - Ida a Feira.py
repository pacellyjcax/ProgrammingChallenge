res = []
n = int(raw_input())
for i in range(n):
    d = {}
    m = int(raw_input())
    for i in range(m):
        en = raw_input().split()
        d[en[0]] = float(en[1])

    o = int(raw_input())
    vT = 0.0
    for i in range(o):
        en = raw_input().split()
        vT += d[en[0]]*int(en[1])
    res.append(vT)
    
for e in res:
    print "R$ %.2f" %e
