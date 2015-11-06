import sys
def caminho(g,ini,fin,vis=[],dis={},rot={}):
    if ini==fin:
        cam=[]
        while fin != None:
            cam.append(fin)
            fin=rot.get(fin,None)
        return dis[ini], cam[::-1]    
    if not vis:
        dis[ini]=0
    for no in g[ini]:
        if no not in vis:
            noDist = dis.get(no,sys.maxint)
            noDistTemp = dis[ini] + g[ini][no]
            if noDistTemp < noDist:
                dis[no] = noDistTemp
                rot[no]=ini
                
    vis.append(ini)
    toVis = dict((k, dis.get(k,sys.maxint)) for k in g if k not in vis)
    minNo = min(toVis, key=toVis.get)
    return caminho(g,minNo,fin,vis,dis,rot)

while 1:
    en = [int(k) for k in raw_input().split()]
    if sum(en) == 0:
        break
    g = dict((k,{}) for k in xrange(1,en[0]+1))
    for i in xrange(en[1]):
        da = [int(k) for k in raw_input().split()]
        g[da[0]][da[1]] = da[2]
        print g
    n = int(raw_input())
    for i in xrange(n):
        try:
            da = [int(k) for k in raw_input().split()]
            print caminho(g,da[0],da[1])[0]
        except:
            print "Nao e possivel entregar a carta"
    print
