r = []
n = int(raw_input())
for i in range(n):
    d = [float(X) for X in raw_input().split()] 
    r.append((d[0]*0.2)+(d[1]*0.3)+(d[2]*0.5))

for e in r:
    print "%.1f"%e
