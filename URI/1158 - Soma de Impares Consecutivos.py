e= int(raw_input())
res = []
for i in range(e):
    d = [int(x) for x in raw_input().split()]
    s = []
    if d[0]%2 == 0:
        s = [x for x in range(d[0]+1,d[0]+(d[1]*2),2)]
    else:
        s = [x for x in range(d[0],d[0]+(d[1]*2),2)]
    res.append(sum(s))

for e in res:
    print e
