n = int(raw_input())
for i in range(n):
    en = raw_input().split()
    v = raw_input().split()
    d = {}
    for j in range(int(en[1])):
        d[str(j+1)] = 0
    for e in v:
        d[e] += 1
    vm = max(d.values())
    if  vm >= ((int(en[1])/2)+1):
        for k,v in d.items():
            if v == vm:
                print k
    else:
        print -1
