res = []
while 1:
    n= int(raw_input())
    if n == 0:
        break
    e = [int(x) for x in raw_input().split()]
    e[e.index(max(e))] = 0
    res.append(e.index(max(e))+1)
    
for e in res:
    print e
