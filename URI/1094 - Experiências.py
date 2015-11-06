d = {"C":0,"R":0,"S":0}

for i in range(int(raw_input())):
    v = raw_input().split()
    d[v[1]]+=int(v[0])

print'''Total: {0:d} cobaias
Total de coelhos: {1:d}
Total de ratos: {2:d}
Total de sapos: {3:d}
Percentual de coelhos: {4:.2f} %
Percentual de ratos: {5:.2f} %
Percentual de sapos: {6:.2f} %'''.format(sum(d.values()),
                                       d["C"],d["R"],d["S"],
                                       (100.0/sum(d.values()))*d["C"],
                                       (100.0/sum(d.values()))*d["R"],
                                       (100.0/sum(d.values()))*d["S"])
