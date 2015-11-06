res = []
for i in range(int(raw_input())):
    raw_input()
    d = {}
    en = raw_input().split()
    for e in en:
        if not d.has_key(e):
            d[e] = 1
        
    res.append(sum(d.values()))
 
for e in res:
    print e
