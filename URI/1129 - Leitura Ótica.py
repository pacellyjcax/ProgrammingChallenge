def verificaQuestao(l):
    v=["A","B","C","D","E"]
    lrm = [x for x in l if x<=127]
    if len(lrm)>1 or len(lrm) == 0:
        return "*"
    return v[l.index(lrm[0])]
res = []
while 1:
    n = int(raw_input())
    if n == 0:
        break
    for i in range(n):
        res.append(verificaQuestao([int(x)for x in raw_input().split()]))

for e in res:
    print e
