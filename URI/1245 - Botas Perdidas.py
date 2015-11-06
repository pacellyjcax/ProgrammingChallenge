def fp(p,l):
    if p == "E" and l.count("D")>0:
        return True
    elif p == "D" and l.count("E")>0:
        return True
    return False
        
    

res = []
while 1:
    try:
        d = {}
        n = int(raw_input())
        tp = 0
        for i in range(n):
            en = raw_input().split()
            if d.has_key(en[0]):
                if fp(en[1],d[en[0]]):
                    tp += 1
                    if en[1] == "E":
                        d[en[0]].remove("D")
                    elif en[1] == "D":
                        d[en[0]].remove("E")
                else:
                    d[en[0]].append(en[1])
            else:
                d[en[0]] = [en[1]]
        res.append(tp)
    except:
        break
    
for e in res:
    print e
