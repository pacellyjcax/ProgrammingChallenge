'''
res = []
while 1:
    n = raw_input()
    if n == "0 0":
        break
    en = [int(x) for x in n.split()]
    df = [0 for i in range(en[0])]
    for i in range(en[1]):
        d = [int(x) for x in raw_input().split()]
        for j in range(len(d)):
            if d[j] == 1:
                df[j] += 1
    if df.count(en[1])>=1:
        res.append("yes")
    else:
        res.append("no")
        
for e in res:
    print e
'''
    
while 1:
    n= raw_input()
    if n == "0 0":
        break
    n = [int(x) for x in n.split()]
    v = [0 for i in range(n[0])]
    for i in range(n[1]):
        es = [int(x) for x in raw_input().split()]
        for i in range(n[0]):
            v[i] += es[i]
    if v.count(n[1])>0:
        print "yes"
    else:
        print "no"
