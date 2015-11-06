def saldoDeGols(l1,l2):
    return (int(l1[0])+int(l2[2])) - (int(l1[2])+int(l2[0]))

def golsNoAdversario(l1,l2):
    if l1[2] > l2[2]:
        return "Time 2"
    elif l1[2] < l2[2]:
        return "Time 1"
    return "Penaltis"


res = []

n = int(raw_input())
for i in range(n):
    p1 = [x for x in raw_input().split()]
    p2 = [x for x in raw_input().split()]

    if saldoDeGols(p1,p2) == 0:
        res.append(golsNoAdversario(p1,p2))
    elif saldoDeGols(p1,p2) > 0:
        res.append("Time 1")
    else:
        res.append("Time 2")
            
for e in res:
    print e
