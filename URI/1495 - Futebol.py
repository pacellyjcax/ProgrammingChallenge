def cpm(l,qt):
    tp = 0
    for e in l:
        if e[0] > e[1]:
            tp += 3
        elif e[0] == e[1] and qt > 0:
            tp += 3
            qt -= 1
    for e in l:
        if e[0]+qt > e[1]:
            tp += 3
            qt -= (e[1]-e[0])+1
        elif e[0]+qt == e[1]:
            tp += 1
    return tp


print cpm([[1,1],[1,1]],1)
print cpm([[1,3],[3,1],[2,2]],2)
'''
res = []
for i in range(int(raw_input())):
    raw_input()
    en = [int(x) for x in raw_input().split()]
    res.append(calculaUltrapassagens(en))

for e in res:
    print "Optimal train swapping takes %d swaps." % e
'''
