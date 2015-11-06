res = []

n = int(raw_input())
for i in range(n):
    d = {}
    m = int(raw_input())
    for j in range(m):
        e = raw_input()
        if d.has_key(e):
            d[e] += 1
        else:
            d[e] = 1      
    for (k,v) in d.items():
        if v < m:
            res.append("ingles")
            break
        elif v == m:
            res.append(k)
            break
        
for e in res:
    print e
