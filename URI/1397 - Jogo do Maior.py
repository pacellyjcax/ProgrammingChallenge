res = []
while 1:
    n = int(raw_input())
    if n == 0:
        break
    a = 0
    b = 0
    for i in range(n):
        e = [int(x) for x in raw_input().split()]
        
        if e[0]>e[1]:
            a+=1
        elif e[0]<e[1]:
            b+=1
    res.append((a,b))

for e in res:
    print str(e[0])+" "+str(e[1])
