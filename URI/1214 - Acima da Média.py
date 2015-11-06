def contaTrocas(l):
    tc = 0    
    for i in range(1,len(l)):
        j = i-1
        t = l[i]
        while j >= 0 and l[j] > t:
            l[j+1] = l[j]
            tc +=1
            j-=1
        l[j+1] = t                
    return tc

res = []
for i in range(int(raw_input())):
    en = [int(x) for x in raw_input().split()]
    qt = en.pop(0)
    medTur = sum(en)/float(qt)
    ac = [x for x in en if x>medTur]
    res.append((len(ac)*100.0)/float(qt))

for e in res:
    print "%.3f" %e +"%"
