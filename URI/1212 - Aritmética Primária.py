def carry(x,y):
    lx = [int(k) for k in str(x)]
    ly = [int(k) for k in str(y)]
    tc = 0
    c = 0
    if len(lx)>len(ly):
        for i in range(len(ly)-1,-1,-1):
            if lx[i]+ly[i]+c > 9:
                tc+=1
                c = 1
            else:
                c = 0
    else:
        for i in range(len(lx)-1,-1,-1):
            if lx[i]+ly[i]+c > 9:
                tc+=1
                c = 1
            else:
                c = 0
    return tc
        

res = []
while 1:
    d = [int(x) for x in raw_input().split()]
    if d[0] == 0 and d[1] == 0 :
        break
    c = carry(d[0],d[1])
    if c == 0:
        res.append("No carry operation.")
    elif c == 1:
        res.append("1 carry operation.")
    else:
        res.append("%d carry operations."%c)
    
for e in res:
    print e
