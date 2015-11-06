res = []
n = int(raw_input())
for i in range(n):
    qt = [int(x) for x in raw_input().split()]
    d = {}
    for t in range(qt[0]):
        d[raw_input()] = [0,0,0,t]

    for j in range(qt[1]):
        dj = raw_input().split()
        if int(dj[0])>int(dj[2]):
            d[dj[1]][0] += 1
            d[dj[1]][2] += 3
        elif int(dj[0])<int(dj[2]):
            d[dj[3]][0] += 1
            d[dj[3]][2] += 3
        elif int(dj[0])==int(dj[2]):
            d[dj[1]][2] += 1
            d[dj[3]][2] += 1
        d[dj[1]][1] += int(dj[0])
        d[dj[3]][1] += int(dj[2])

    while len(d.values()) > 0:
        mp = max([x[2] for x in d.values()])
        emp = [k for k in d.keys() if d[k][2] == mp]
        if  len(emp) > 1:
            mv = max([d[x][0] for x in emp])
            emp = [k for k in emp if d[k][0] == mv]
            if len(emp) > 1:
                mg = max([d[x][1] for x in emp])
                emp = [k for k in emp if d[k][1] == mg]
                if len(emp) > 1:
                    oe = min([d[x][3] for x in emp])
                    emp = [k for k in emp if d[k][3] == oe]
        res.append(emp[0])
        d.pop(emp[0])

for e in res:
    print e
            
