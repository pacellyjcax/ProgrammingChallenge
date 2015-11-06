def ehPrimo(i):
    if len([x for x in range(2,i) if i%x ==0])>0:
        return False
    return True
    
e= int(raw_input())
res = []
for i in range(e):
    d = int(raw_input())
    if ehPrimo(d):
        res.append("%d eh primo" %d)
    else:
        res.append("%d nao eh primo" %d)

for e in res:
    print e
