res = []
while 1:
    n= int(raw_input())
    if n == 0:
        break
    d = {}
    for i in range(n):
        e = raw_input().split()
        d[e[0]] = int(e[1])-int(e[2])
    m = min(d.values())
    for k,v in d.items():
        if v == m:
            res.append(k)
            break
    
for e in res:
    print e
