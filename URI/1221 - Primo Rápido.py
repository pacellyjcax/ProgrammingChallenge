import math
def ehPrimo(i):
    if i%2 ==0:
        return False
    rqi = math.ceil(math.sqrt(i))
    for x in xrange(3,int(rqi),2):
        if i%x ==0:
            return False
    return True

e= int(raw_input())
res = []
for i in xrange(e):
    d = int(raw_input())
    if ehPrimo(d):
        res.append("Prime")
    else:
        res.append("Not Prime")

for e in res:
    print e

