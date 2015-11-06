def agrupa(l1,l2):
    lf = []
    for i in range(min(len(l1),len(l2))):
        lf.append(l1[0])
        l1 = l1[1:]
        lf.append(l2[0])
        l2 = l2[1:]
    if len(l1)>0:
        return "".join(lf)+l1
    return "".join(lf)+l2

res = []

n = int(raw_input())
for i in range(n):
    en = [x for x in raw_input().split()]
    res.append(agrupa(en[0],en[1]))

for e in res:
    print e
