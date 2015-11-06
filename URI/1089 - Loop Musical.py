null = -9999999
while 1:
    n = int(raw_input())
    if n == 0:
        break
    c = 0
    pa = null
    sa = null
    si = null
    sf = null
    nn = n
    s = 0
    dados = [int(x) for x in raw_input().split()]
    for i in xrange(n):
        e = dados[i]
        if not pa == null:
            if pa < e:
                s = 1
            elif pa > e:
                s = -1
                if not sa == null:
                    if sa != 0 and s != sa:
                        c+=1
                sa = s
            pa = e
            if si == null and s != 0:
                si = s
            if nn == 0:
                sf = s
        if not si == sf:
            c+=1
        elif si == sf and  not si == 0:
            c += 2

    print c
        
'''
while 1:
    n = int(raw_input())
    if n == 0:
        break
    b = map(int,raw_input().split())
    cont = 0;
    if b[n - 1] > b[0] and b[1] > b[0]:
        cont += 1
    elif b[n - 1] < b[0] and b[1] < b[0]:
        cont += 1    
    if b[n - 2] > b[n - 1] and b[0] > b[n - 1]:
        cont += 1
    elif b[n - 2] < b[n - 1] and b[0] < b[n - 1]:
        cont += 1    
    for i in xrange(n-1):
        if b[i - 1] > b[i] and b[i + 1] > b[i]:
            cont += 1
        elif b[i - 1] < b[i] and b[i + 1] < b[i]:
            cont += 1
    print cont
'''
#WA50%
'''
def calcula (b):
    vf = 0
    if len(b)==2:
        if b[0]!= b[1]:
            return 2
        return 0
    elif len(b)==1:
        return 0
    for i in range(1,len(b)-1):
        if b[i] < b[i-1] and b[i] < b[i+1]:
            vf+=1
        elif b[i] > b[i-1] and b[i] > b[i+1]:
            vf+=1
    if b[0] > b[1] and b[1] < b[2]:
        vf+=1
    elif b[0] < b[1] and b[1] > b[2]:
        vf+=1            
    if b[len(b)-1] < b[len(b)-2] and b[len(b)-1] < b[0]:
        vf+=1
    elif b[len(b)-1] > b[len(b)-2] and b[len(b)-1] > b[0]:
        vf+=1
    return vf


it = []
while 1:
    n = int(raw_input())
    if n == 0:
        break
    b = raw_input().split()
    it.append([int(x) for x in b])

for e in it:
    print calcula(e)

    
'''
