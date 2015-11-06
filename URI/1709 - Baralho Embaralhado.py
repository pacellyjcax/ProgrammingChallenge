def emb(l):
    l1 = [l[i] for i in range(len(l)/2)]
    l2 = [l[i] for i in range(len(l)/2,len(l))]
    lf = []
    for i in range(len(l1)):
        lf.append(l1[i])
        lf.append(l2[i])
    return lf

bi = [str(x) for x in range(int(raw_input()))]
b = [x for x in bi]
c = 0
while 1:    
    b = emb(b)    
    if b == bi:
        break
    c += 1
print c
