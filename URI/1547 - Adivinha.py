def modulo(i):
    if i<0:
        return i*(-1)
    return i

res = []

n = int(raw_input())
for i in range(n):
    vd = int(raw_input().split()[1])
    vs = [modulo(vd - int(x)) for x in raw_input().split()]
    res.append(vs.index(min(vs))+1)
            
for e in res:
    print e
