def vence(ds):
    s = sum(ds)
    if s == 1:
        return pos[ds.index(1)]
    elif s == 2:
        return pos[ds.index(0)]
    return "*"

pos = ["A","B","C"]       
res = []

while 1:
    try:
        res.append(vence([int(x) for x in raw_input().split()]))
    except:
        break

for e in res:
    print e
