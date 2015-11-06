  
e= int(raw_input())
res = []
for i in range(e):
    d = float(raw_input())
    c = 1
    while d>c:
        d*=0.5
        c +=1
    res.append(c)
    
for e in res:
    print "%d dias" %e
