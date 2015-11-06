def calc(l):    
    return (l[3]-l[1])/(l[2]-l[0])

e= int(raw_input())
res = []
for i in xrange(e):
    d = [float(x) for x in raw_input().split()]
    res.append(str(calc(d)))
for e in res:
    a = e.split(".")
    if len(a[1]) == 1:
        print a[0]+","+a[1]+"0"
    else:
        print a[0]+","+a[1][:2]

